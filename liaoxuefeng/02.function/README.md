# 函数
Python内置了很多函数，可以使用`help(function)`查看帮助信息。    
调用函数的时候，如果参数不正确，会抛出`TypeError`的异常，我们可以捕捉异常进行下一步处理。    
Python内置的常用数据类型的函数可以进行类型转换，比如`int(), float(), etc.`。    
Python中一切皆对象，包括函数。函数名其实就是一个函数对象的引用，函数名可以直接赋值给一个变量。    

## 自定义函数
使用`def function(parameter_list)`就可以定义一个函数。    
定义一个什么也不做的空函数体的函数，使用`pass`关键字，这个关键字也可以用作占位符。    
定义函数时，需要确定函数名称和参数的个数，必要时，需要对参数进行类型检查。   
函数可以用`return`来返回结果值，如果函数没有`return`结果，默认按照`return None`来处理。    

## 默认参数
函数参数使用`function(parameter = default)`格式就带有默认参数。   
函数参数必选参数在参数列表的最前面，默认参数必须在最后面。    
函数的默认参数必须指向不变的对象，不然默认参数会失效。   

## 可变长度参数
函数参数使用`function(*variable_parameter)`格式带有可变长参数。    
可变长参数Python处理时会组装成一个`tuple`进行参数转换。   
如果想指定`key:value`形式的参数，使用格式`function(**key_value)`的方式进行定义。    
因此，函数`function(*args, **key_values)`可以被任意形式调用。   

## 递归函数
如果一个函数调用自己本身，就称这个函数为递归函数。    
理论上，所有的递归函数都可以写成循环方式，但是逻辑不清晰。   
定义递归函数时，需要注意栈溢出，因此边界（基准情况）很重要。    

# 练习
1. 定义一个函数，接收三个参数`a, b, c`，返回一元二次方程`ax^2 + bx + c`的两个根。
2. 使用递归玩汉诺塔游戏（A, B, C三根柱子，最开始A上面有N个盘子）。
