# 面向对象高级编程
创建一个类的实例之后，我们可以给这个实例绑定任何属性和方法，这就是动态语言的灵活性。    
但是注意以上说明，给一个实例绑定的属性和方法对另外一个实例不可用。     

	>>> student = Student()
	>>> student.name = 'Lilei'
	>>> student.name
	>>> 'Lilei'
	>>> def age(self, age):
		... self.age = age
	>>> from types import MethodType
	>>> student.age = MethodType(age, student)
	>>> student.age(18)
	>>> student.age
	>>> 18

## 限定外部定义属性
Python中类定义时使用`__slots__`变量来限定一个类可以在外部添加的属性，该变量的值是一个tuple。    
当外部绑定属性时被`__slots__`限定时，抛出`AttributeError`的异常。    
`__slots__`属性只对当前类的实例起作用，对继承的子类的实例不起作用。    

	class Student:
		# 限定只能在外部绑定name和age属性 
		__slots__ = ('name', 'age')


## 类的属性getter/setter
既能让类的属性进行输入参数检查，又能像外部添加属性一样方便的添加属性。    
`@property`装饰器就是负责把一个类的方法当成属性一样访问。    

	class Student(object):
		@property
		def age(self):
			return self.__age;

		@age.setter
		def age(self, age):
			if not isinstance(age, int):
				raise TypeError('invalud type of input age.')

			if age > 100 or age < 0:
				raise ValueError('age must be between 0 ~ 100.')

			self.__age = age

	>>> student = Student()
	>>> student.age = 18
	>>> student.age
	>>> 18
	>>> student.age = 1000
	....
	ValueError: age must be between 0 ~ 100.

## 多重继承
多重继承时，主线是单一继承下来的，对于需要的其他功能可以写`MixIn`类来进行多重继承，从而达到给类添加功能的目的。    

## 定制类
`__str__(self)`函数可以通过友好字符串的方式展示类的内容。     
`__repr__(self)`函数可以通过调试字符串的方式展示类的内容。    
`__iter__(self)`函数可以进行迭代。    
`__next__(self)`函数可以进行迭代取值。    
`__getitem__(self, index)`函数可以进行对象的下标访问。    
`__getattr__(self, name)`函数可以定制属性没有时返回的值，避免异常。    
`__call__(self, parameters)`函数可以让类实例作为函数名称，并且加以参数调用。    

## 枚举
定义具有枚举性质的大量常量时可以使用枚举类。    
枚举类的定义值默认从`1`开始。    

	from enum import Enum
	month = Enum('month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
				'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
	for name, member in month.__members__.items():
		print(name, ' --> ', member.value)

如果需要更精确的控制枚举类型的值，可以定义一个继承`enum.Enum`的类，并且用`@unique`装饰器检查值的唯一性。    
	
	from enum import Enum, unique

	@unique
	class WeekDay(Enum):
		Sun = 0
		Mon = 1
		Tue = 2
		Wed = 3
		Thu = 4
		Fri = 5
		Sat = 6

## type()函数
`type()`函数可以查看一个类型或者一个变量的类型。  
`type()`函数也可以创建一个新的类型，比如创建一个简单的类：    

	>>> def func(self, name = 'world'):
		... 	print('hello, ', name)
		...
	>>> Hello = type('Hello', (object,), dict(hello = func))
	>>> h = Hello()
	>>> h.hello()
	hello,  world

`type()`函数创建新类型的参数：
1. class的名称
2. 继承的父类的集合，是一个tuple，单个tuple写的时候第一个元素后要加`,`
3. class的方法名称和函数绑定，用dict

## 元类
当我们定义类之后，根据类可以生成实例，也就是说实例是类创建出来的。    
那么有一个问题：类是什么创建出来的呢？或者说我们要动态创建类呢？    
元类`metaclass`可以创建类，也可以修改类。    
元类是类的模板，因此必须要继承于`type`类。

	# 我们给原有的Sample类添加一个属性
	class SampleMetaClass(type):
		def __new__(cls, name, bases, attrs):
			attrs['add'] = lambda self, value: self.append(value)
			return type.__new__(cls, name, bases, attrs)

	class Sample(metaclass = SampleMetaClass):
		pass

以上就直接实现了每个`Sample`类的实力都已经有一个`add(self, value)`方法了。    
类生成对象调用`__new__()`函数，参数解析：
1. cls是当前准备创建的类的实例的名称
2. name是当前类的名称
3. bases是当前类继承的父类的集合
4. attrs是当前类的方法集合

Q：直接在类定义里面添加这个方法不行么，非要用元类？      
A：总有不行的情况出现，比如在使用之前都不知道的类方法。        
Q：再举个例子说明一下这个场景？                
A：比如实现所有的场景的用户数据插入数据库的场景：
1. 用户类插入时字段有用户名，密码，性别等；
2. 评论类插入时字段有评论对象标识，评论文章标识，评论内容，评论时间等；
3. 还有其他更新等操作；
             
**但是不管元类多好，因为可以直接修改类，因此谨慎使用！**

## 练习
1. 给`Screen`加上属性`height`和`width`，以及计算分辨率`resolution`。
2. 使用元类编写一个用户类，并且`save()`函数实现数据库`insert`语句。

