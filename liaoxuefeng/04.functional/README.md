# 函数式编程
函数就是面向过程程序设计的基本单元。    
前面就已经了解过，函数的名称也是一个变量，可以作为参数传入另一个函数。    

## 高阶函数
函数的参数中有另外的函数的函数名作为参数，那么这个函数就称为高阶函数。    

	def sample(func, x, y):
		return func(x) + func(y)

上述这个函数就是一个很简单的高阶函数。    

## map函数
Python内建了`map()`函数，函数的第一个参数是函数，第二个参数是一个可迭代对象`Iterable`。    
`map()`函数的作用就是将参数传入的第一个函数依次作用于第二个可迭代对象参数的每一个元素。    

	map(func, [x, y, z]) = [func(x), func(y), func(z)]

比如：将一个数字列表转换成字符串
	
	>>> list(map(str, [1,2,3,4,5]))
	>>> ['1','2','3','4','5']

## reduce函数
Python内建了`reduce()`函数，函数的第一个参数是函数，第二个参数是一个可迭代对象`Iterable`。    
`reduce()`函数的作用就是将参数传入的第一个函数逐层作用于第二个可迭代对象的每个元素。    

	reduce(func, [x, y, z]) = func(func(x, y), z)

比如：将一个数字列表求和

	>>> from functools import reduce
	>>> reduce((lambda x, y: x + y), [1, 2, 3, 4, 5])
	>>> 15

## filter函数
Python内建了`filter()`函数用于过滤序列，函数的第一个参数是函数，第二个参数是一个可迭代对象`Iterable`。    
`filter()`函数的作用就是根据第一个参数函数的返回值是`True`还是`False`作用于第二个可迭代对象是保留还是删除。     
比如：将一个数字列表中的偶数去掉    

	>>> list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6]))
	>>> [1, 3, 5]

## sorted函数
Python内建的`sorted()`函数可以给一个序列排序，函数的第一个参数是列表，第二个参数是实现排序的函数`key`。    
如果`key`函数指定了函数，那么会作用第一个参数列表中的每一个元素，然后按照结果再排序。    
比如：将一个数字列表按照绝对值排序

	>>> sorted([1, -3, 2, 4], key = abs)
	>>> [1, 2, -3, 4]

## 返回函数
高阶函数除了可以接受函数作为参数之外，还可以将函数作为结果变量返回出去。    
比如：写一个不立即求值的不定参数的加法运算    

	def lazy_sum(*args):
		def sum():
			result = 0
			for item in args:
				result = result + item
			return result
		return sum

## 闭包
从上面的例子可以看到，返回的函数内部使用了局部变量，当函数返回之后，里面的局部变量还会被新函数引用。   
需要注意的一个问题，闭包中返回的函数没有立即执行，而是直到调用的时候才执行，因此这地方需要特别注意。    
举个例子：    

	def count():
		result = []
		for item in range(1, 4):
			def func():
				return item * item
			result.append(func)
		return result

然后引用`count()`函数，我们发现：

	>>> count1, count2, count3 = count()
	>>> count1()
	>>> 9
	>>> count2()
	>>> 9
	>>> count3()
	>>> 9

以上问题的原因：就是闭包中的函数在调用时才执行，调用时循环变量`item`都已经变成了`3`，那么结果就是`9`。    
因此，闭包中的函数尽量不引用循环变量，如果非要引用，外层需要新增加另外一个函数作为过渡。    

## 偏函数
Python的`functools`提供了很多有用的函数，其中一个是偏函数（Partial Function）。    
偏函数的作用就是把一个函数的某些参数给固定住，返回一个新的函数，这样这个函数的调用就简单一些。    
比如`int()`函数就是把一个字符串转换成整型，比如不同进制的转换如下：    

	>>> int('10101')   # 默认按照十进制转换
	>>> 10101
	>>> int('10101', base=2)   # 显式指定按照二进制转换
	>>> 21

如果我们一直用二进制的话，每次都写`int(x, base='2')`就显得很麻烦，我们可以定义一个`int2(x)`专门处理这种情况：    

	>>> def int2(x):
		... return int(x, base=2)

`functools`中提供了`functools.partial`功能，可以简化上述操作：

	>>> import functools
	>>> int2 = functools.partial(int, base=2)

## 装饰器
前面已经说过，Python中函数也是一个对象，每个函数有个`__name__`属性，指示自己的名称。    
需要增强函数的功能，同时又不改变函数的定义，动态增强函数功能的部件，称之为装饰器`Decorator`。    
本质上，装饰器就是一个返回函数的高阶函数。   

	def log(func):
		def wrapper(*args, **kw):
			print('call ', func.__name__)
			return func(args, kw)
		return wrapper

上面这种方式，就形成了一个装饰器。    
原有的函数`func`继续执行自己本身，`wrapper`来增强`func`的功能：打印调用轨迹。    
调用装饰器时，用到Python的`@`装饰器方式，将装饰器置于函数的定义处。    

	@log
	def hello():
		return 'hello'

经过装饰器装饰过的函数，就上面这个例子来说，`hello.__name__`已经变成了`wrapper`。    
这样函数名称发生了变化，那代码中有依赖函数签名的地方会报错，因此有了`functools.wraps`。    
上面的代码用`functools.wraps`变更如下：    

	import functools
	def log(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('call ', func.__name__)
			return func(args, kw)
		return wrapper

## 练习
1. 用`map()`函数将list中的字符串首字母大写。
2. 用`map()`和`reduce()`函数实现字符串转换成浮点型数字。
3. 用`filter()`函数筛选出一个列表中的回数【回数就是从左向右还是从右向左读都一样的数字，比如12321】。
4. 用闭包实现一个计数器。
5. 设计一个装饰器，作用于任何函数之上，打印出该函数执行的时间。    
