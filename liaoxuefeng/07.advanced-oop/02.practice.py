# _*_ coding: utf-8

# 首先定义数据库的字段类，包括字段名和字段类型属性
class Field(object):
	def __init__(self, name, column_type):
		self._name = name
		self._column_type = column_type

	def __str__(self):
		return '%s:%s %s' % (self.__class__.__name__, self._name, self._column_type)

# 定义数据库类的字符串类
class StringField(Field):
	def __init__(self, name, column_length):
		# 调用基类的构造函数
		super(StringField, self).__init__(name, 'varchar2')
		self._column_length = column_length

	def __str__(self):
		return '<%s[%d]>' % (super(StringField, self).__str__(), self._column_length)

# 定义数据库类的整型类
class IntegerField(Field):
	def __init__(self, name, column_length):
		super(IntegerField, self).__init__(name, 'number')
		self._column_length = column_length

	def __str__(self):
		return '<%s[%d]>' % (super(IntegerField, self).__str__(), self._column_length)

# 定义数据库表名
class TableNameField(Field):
	def __init__(self, name):
		super(TableNameField, self).__init__(name, 'varchar2')

	def __str__(self):
		return '<table[%s]>' % super(TableNameField, self).__str__()

# 定义模型类的元类
class ModelMetaClass(type):
	def __new__(cls, name, bases, attrs):
		# 排除对模型类的修改，当模型类无法创建对象时会调用父类元类来进行创建的
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)

		print('Already found model: ', name)
		mappings = dict()
		table = None
		for key, value in attrs.items():
			if isinstance(value, Field):
				print('Already found mapping: %s --> %s' % (key, value))

				# 属性中不存放表名
				if not isinstance(value, TableNameField):
					mappings[key] = value
				else:
					table = value

		# 这地方为什么要弹出key值：
		# 元类使用创建类的时候，元类的new方法要先于类的new方法执行执行
		# 比如创建出的类创建实例的时候，getattr的顺序是类的属性，父类的属性
		# 如果这地方不弹出，那么会在元类创建的类中有这个属性值，这个属性值很可能不是想要的
		# 在调用的时候，getattr会找对应的属性，这时候元类生成的类就需要定义自己的getattr获取值
		for key in mappings.keys():
			attrs.pop(key)

		# 保存属性和列的关系
		attrs['__mappings__'] = mappings
		attrs['__table__'] = table._name
		return type.__new__(cls, name, bases, attrs)

# 定义模型类
class Model(dict, metaclass = ModelMetaClass):
	def __init__(self, **kw):
		# 调用父类，也就是dict的构造函数进行构造
		super(Model, self).__init__(**kw)

	# 定义自己的getattr，原因在元类中已经说明
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError('class [%s] has no attribute [%s]' % (self.__class__.__name__, key))

	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fields = []  # 字段名称
		params = []  # 占位符
		args = []    # 具体的参数值

		for key, value in self.__mappings__.items():
			fields.append(value._name)
			params.append('?')
			args.append(getattr(self, key, None))

		sql = 'insert into %s (%s) values (%s)' % (
				self.__table__, ', '.join(fields), ', '.join(params))
		return sql, args

# 定义用户信息类
class UserInfo(Model):
	# 定义类的属性字段
	table = TableNameField('user_info')
	user_id = IntegerField('user_id', 16)
	user_name = StringField('user_name', 32)
	user_gender = IntegerField('gender', 1)
	user_email = StringField('email', 32)
	user_passwd = StringField('password', 128)

if __name__ == '__main__':
	user = UserInfo(user_id = 1001, 
			user_name = 'Lilei',
			user_gender = 1,
			user_email = 'Lilei.xxx@python.com',
			user_passwd = 'Ft565324%$^$dsadaw@#$#%^$,.va')

	sql, args = user.save()
	print('save user information statement and parameters: ')
	print('sql: ', sql)
	print('parameters: ', str(args))

