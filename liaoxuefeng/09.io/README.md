# IO编程
IO在计算机中指的是Input/Output，由于程序运行时的数据是在内存中，因此涉及到数据交换的地方，比如磁盘，网络等，就需要IO接口。    
IO编程中，流（Stream）是一个很重要的概念，可以理解为水管，数据就是水管中的水，只能单向流动。    
Input Stream就是数据从外部（比如磁盘，网络等）流进内存；Output Stream就是数据从内存流到外部。    

## 文件读写
Python中内置了文件读写的函数，用法和C兼容。    
Python内置的`open()`函数进行打开一个文件，返回一个文件对象，文件不存在抛出`IOError`的异常。    
文件对象的`read()`方法可以一次读取文件的全部内容。    
文件对象的`read(size)`方法可以读取`size`字节的文件内容。    
文件对象的`readline()`方法可以每次读取文件的一行内容。    
文件对象的`readlines()`方法可以按照行读取全部文件内容，并且保存在一个list中。    
文件对象的`write()`方法可以将内容写入文件。    
文件对象的`close()`函数进行关闭文件。    

	try:
		file_obj = open(file_path, open_mode, file_encoding)
		print(file_obj.read())
	finally:
		if file_obj:
			file_obj.close()

每次按照上述的步骤读写文件感觉很繁琐，因此Python引入了`with`语句来简化，最后不必调用`close()`方法关闭文件：

	with open(file_path, open_mode) as file_obj:
		print(file_obj.read())

## StringIO
很多时候，数据读写的对象不一定是文件，也有可能是内存中读写。    
StringIO就是在内存中读写数据。    
StringIO的读写非常简单，就是创建一个StringIO对象，然后用文件读写的方式进行读写即可。    
StringIO对象的`getvalue`的方法可以获取写到StringIO对象中的内容。    

	from io import StringIO
	sio = StringIO()
	sio.write('hello')
	print(sio.getvalue())

## BytesIO
StringIO只能操作str对象在内存中的读写，BytesIO操作二进制对象在内存中的读写。    

## 操作文件和目录
Python程序中需要操作文件和目录，就需要引入os模块。    
`os.name()`的结果如果是`posix`，就说明是Linux为内核的系统；`nt`就表示Windows系统。    
`os.uname()`可以获取详细的系统信息（Windows上不提供，因此os模块和操作系统有关系）。    
`os.environ`这个变量存储着环境变量信息，使用`os.environ.get(key)`的方式获取`key`对应的环境变量。    
`os.mkdir(path)`创建一个路径。    
`os.rmdir(path)`删除一个路径。    
`os.rename(file1, file2)`重命名一个文件。    
`os.remove(file)`删除一个文件。    
`os.path.isdir(path)`判断路径是否是一个目录。    
`os.listdir(path)`列举出路径下面的路径和文件。    
`os.path.abspath(.)`返回当前路径的绝对路径。   
`os.path.join(path1, path2)`返回当前两个路径合并的结果，会在路径中间添加`/`，这样会根据不同的操作系统生成对应的路径。    
`os.path.split(path)`返回拆分的路径，后一部分是路径最后的级别（可能是路径，也可能是文件名）。    


## 序列化
我们把变量从内存中变成可存储或者可传输的过程称之为序列化。    
序列化之后，就可以把序列化的内容写到磁盘上，或者进行网络传输等。    
把变量从序列化的对象重新读取到内存的过程称之为反序列化。    
Python提供了模块`pickle`来进行序列化对象。    
`pickle.dump(obj, file)`把对象序列化到文件中。    
`pickle.load(file)`把对象从文件中反序列化到内存中。    

### 序列化之JSON
模块`json`提供了非常完美的Python对象到Json格式的转换。    
`json.dumps(obj, file)`可以将对象序列化到文件。    
`json.loads(file)`可以从文件中进行反序列化出对象。    


