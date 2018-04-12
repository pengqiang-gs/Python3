# Python基础
Python是一种计算机编程语言。    
Python的语法比较简单，采用缩进的方式进行代码块组织。    
Python的注释以`#`开头，可以单独一行，或者在行尾。    
Python大小写敏感。    

# 数据类型
## 整数
1. 二进制
2. 十进制
3. 十六进制

## 浮点数
整数运算永远是精确的，浮点数有误差。     

## 字符串
使用`\`进行字符串中的特殊字符的转义。

## 布尔值
布尔值只有`True/False`两种取值。

## 空值
Python中控制用`None`表示。

# 字符串编码
世界上有上百种语言，每一种语言的字符串混合在一起，就出现字符串乱码；    
Unicode把所有语言都统一到一套编码中，用两个字节表示一个字符，但是全英文的存储和传输上很不划算；    
UTF-8编码是可变长的Unicode编码，如果英文偏多，那么可以节省空间。    
      
Python3 版本中，字符串是用Unicode编码的，也就是说Python3 版本中的字符串支持多语言。    
Python3 中提供`ord()`函数获取字符的整数表示，`chr()`函数获取整数对应的字符。  
	>>> ord('x')
	120
	>>> ord('爱')
	29233
	>>> chr(99)
	'c'
	>>> chr(30000)
	'田'
字符串可以通过`encode(encoding)`函数进行编码为指定的bytes字符。    
	>>> '你好'.encode('utf-8')
	b'\xe4\xbd\xa0\xe5\xa5\xbd'
	>>> 'abc'.encode('utf-8')
	b'abc'

# list和tuple
## list
list 是列表，可以随时添加和删除列表中的元素。   
函数`len(list)`可以获取列表的长度。    
索引`[index]`可以访问列表中的元素，索引一直是`0`开始，`index`是正数则顺数取值，负数则倒数取值。    
函数`list.append(element)`可以给列表末尾添加元素。    
函数`list.insert(index, element)`可以给列表制定位置添加元素。    
函数`list.pop()`可以返回列表末尾的元素，并且删除。    
函数`list.pop(index)`可以返回列表索引位置的元素，并且删除。    
## tuple
tuple 是元组，一经初始化则不可以更改。

# 条件判断
程序设计的分支结构：`if ... elif ... else ...`。    
	if <condition1>:
		statement1
	elif <condition2>:
		statement2
	else:
		statement3
## 练习1
1. 根据BMI公式（体重除以身高的平方）计算BMI指数，并且根据BMI指数进行以下提示：    
* 低于18.5： 过轻
* 18.5 - 25： 正常
* 25 - 28： 过重
* 28 - 32： 肥胖
* 高于32：严重肥胖

# 循环
一种是 `for ... in ... : statement` 循环；     
一种是 `while <condition> : statement` 循环。    
循环中，`break`可以提前退出循环，`continue`	可以跳过本次循环。

# dict
Python 中内置了dict，也称为 字典/映射，使用`key-value`方式存储，具有很快的查找速度。   
多次给同一个key值赋值，则新值会覆盖原来的旧值。    
判断key存不存在，有两种方式：
1. 使用`if key in dict`方式进行判断；
2. 使用`dict.get(key, None)`方式判断结果是否为None。
使用`dict.pop(key)`可以从dict中删除某一对`key-value`值，也就是dict的一个元素。    
和list比较，dict有以下特点：
1. dict查找和插入速度快，不会因为key值的增多而变慢；
2. dict需要占用的内存比list大。    

# set
Python 中内置了set，也称为 集合，和dict相比较只存储key，所以set中没有重复的key。    
使用`set.add(key)`给set中添加元素。    
使用`set.remove(key)`删除set中的元素。
