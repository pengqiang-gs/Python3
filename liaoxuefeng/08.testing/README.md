# 调试和测试
在程序运行中，总会遇到各种各样的错误：
* 比如程序编写的逻辑发生错误，预期输出整数，结果输出字符串；
* 比如用户输入造成的，比如输入手机号码，结果输入了邮箱；
* 比如无法预计的其他类错误，例如空间磁盘满了等情况；
* 等等

## 错误处理
### 返回值报告错误
利用函数的返回值来报告这个函数是否运行正常。      
使用这种方式会使函数本身正常的返回结果和异常结果混在一起，需要用大量的代码来判断。    
一旦出错，还要一级一级上报，直到某个函数可以处理这类错误。    

### 异常
高级语言中都有异常机制，Python也不例外。    

	try：
		# 可能会出现异常的代码段
	except:
		# 针对发生异常的处理
	else:
		# 针对没有异常的处理
	finally:
		# 不管是否发生异常，都需要的处理

使用异常的最大的好处，就是跨越多层调用，比如嵌套很深的代码，只要外层可以捕捉住异常就可以了。    

### 记录错误
Python的`logging`类可以很方面的记录异常的错误信息。   

	import logging

	def function():
		try:
			statement
		except Exception as e:
			logging.exception(e)

		other_statement

`logging`最大的好处就是程序记录完毕异常之后，可以继续执行下面的代码逻辑而不影响。    

## 调试
### 打印
通过`print()`函数进行打印怀疑有问题的变量。    

### 断言
通过`assert`的方式进行断言，断言为`True`，则直接抛出`AssertionError`的异常。    

	def function(string):
		number = int(string)
		assert number != 0 'number is zero!'
		return 100 / number

断言太多，代码冗余增大，启动的时候可以添加`-O`参数进行失效断言。   

### 日志
上面已经说过，使用`logging`的方式进行输出错误信息而不影响程序运行。    
`logging`有以下的级别进行选择：
* debug：调试级别，所有的日志都会打印出来
* info：信息级别，除了debug级别其他的日志都会打印出来
* warning：警告级别，只打印警告和错误日志
* error：错误级别，只打印错误日志

	import logging
	logging.basicConfig(level=logging.INFO)

### 跟踪
使用`pdb`模块进行单步地跟踪程序，对于查看问题帮助很大。    


### 使用IDE
虽然这种方式很高效，但是个人不喜欢，还是喜欢文本编辑器（比如`Vim`）来编写程序。    

## 单元测试
Python自带的`unittest`模块可以进行单元测试。    
编写单元测试案例类时，需要从`unittest.TestCase`类继承。    
以`test_`开头的方法就是测试方法，否则不会认为是测试方法，测试的时候不会被执行。     
以`unittest.main()`方法进入运行单元测试。   
单元测试类中写`setUp()`和`tearDown()`方法，这个方法可以在每调用一个测试方法前后执行，比如数据库的连接和释放可以写到里面。    

## 文档测试
Python内置的`doctest`模块可以直接提取注释中的代码并且执行测试。    
`doctest`严格按照Python中的交互式命令行的输入输出来判断程序是否正确。    

## 练习
1. 编写一个阶乘函数`factor(number)`并且用`doctest`进行测试。   
