# Python内置模块
Python有很多内置的模块，可以很方便的进行使用。    

## datetime
`datetime`模块是Python处理日期和时间的标准库。   
`datetime.datetime()`表示的时间需要时区信息才能确定一个特定的时间，不然只认为是本地时间。    
`datetime.datetime`存储时最好使用`timestamp`，因为时间戳和时区无关。    

1. `datetime.datetime.now()`获取当前时间。    
2. `datetime.datetime(year, mon, day, hour, min, sec)`获取一个指定的时间。    
3. `datetime.datetime.timestamp()`可以将一个`datetime`对象转换成`timestamp`对象。    
4. `datetime.datetime.fromtimestamp(t)`可以将一个`timestamp`对象转换成本地`datetime`对象。    
5. `datetime.datetime.utcfromtimestamp(t)`可以将一个`timestamp`对象转换成UTC`datetime`对象。     
6. `datetime.datetime.strptime(str, format)`可以将一个字符串转换成`datetime`对象。    
7. `datetime.datetime.strftime(format)`可以将一个时间按照格式转换成字符串。    
8. `datetime.timedelta(key=value)`可以进行时间的加减，`key`可以是年月日时分秒。    
9. `datetime.timezone(key=value)`可以创建一个时区。    

## collections
`collections`模块是Python处理各种集合类的标准库。    

### namedtuple
`namedtuple`是一个函数，专门用来创建一个自定义的tuple类对象，并且规定tuple元素的个数。    
	>>> from collections import namedtuple
	>>> Circle = namedtuple('Curcle', ['radius'])
	>>> c = Circle(2)
	>>> c.radius
	2

### deque
`list`是线性存储的，按照下标访问很快，但是插入和删除就很慢。    
`deque`是双向列表，可以高效的进行插入和删除。    
`deque.append()`函数在`deque`的尾部进行插入。    
`deque.appendleft()`函数在`deque`的头部进行插入。    
`deque.pop()`函数在`deque`的尾部进行删除。    
`deque.popright()`函数在`deque`的头部进行删除。    
	>>> from collections import deque
	>>> queue = deque([1, 2, 3])
	>>> queue
	deque([1, 2, 3])
	>>> queue.append(4)
	>>> queue
	deque([1, 2, 3, 4])
	>>> queue.pop()
	4
	>>> queue
	deque([1, 2, 3])
	>>> queue.appendleft(5)
	>>> queue
	deque([5, 1, 2, 3])
	>>> queue.popleft()
	5
	>>> queue
	deque([1, 2, 3])

### defaultdict
`dict`如果`key`不存在，会抛出`KeyError`的异常，如果不想要异常，可以使用`defaultdict`进行不存在的`key`值默认值设定。    
	>>> from collections import defaultdict
	>>> d = defaultdict(lambda: 'NULL')
	>>> d['key1'] = 'value1'
	>>> d['key1']
	'value1'
	>>> d['key2']
	'NULL'

### OrderedDict
`dict`的`key`值默认是无序的，`OrderedDict`提供了有序`key`值的`dict`。     
`OrderedDict`的`key`会按照插入顺序排列，并不是按照`key`的大小。    

### Counter
`Counter`是一个简单的计数器。    
	>>> from collections import Counter
	>>> cc = Counter()
	>>> for item in 'hello world':
	...     cc[item] = cc[item] + 1
	...
	>>> cc
	Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

## Base64
`Base64`是一种用64个字符表示任意二进制数据的方法。    
用文本编辑器打开`exe`等这种二进制文件时，看到有一大堆乱码，是因为二进制包含很多无法显示和打印的字符。如果用文本编辑器来编辑二进制文件，处理二进制数据，就需要一个二进制向字符串的转换方法。`Base64`就是最常用的方法。    

### Base64原理
1. 准备一个包含64个字符的数组：     
	['A', ..., 'Z', 'a', ..., 'z', 0, ..., 9, '+', '/']     
2. 开始处理二进制数据，每3个字节一组，这3个字符一共是24bit，这一组又分为4个小组，每组就是6bit；    
3. 4个小组中的6bit正好对应一个64以内的数字，这个数字作为上面数组的下标，获取对应的字符；    
4. 二进制数据全部按照上面的步骤1-3处理完毕之后的字符串就是`Base64`编码后的字符串。    

`Base64`编码把原来二进制文件中3个字符的文件编码成4个字符，因此长度增加了1/3，不过编码后的二进制文件内容可以直接传输使用。如果编码的文件长度不是3的倍数，`Base64`会用`\x00`字节在末尾补齐，编码之后的末尾加上1个或者两个`=`号，表示最后编码补齐了几位，解码的时候，会自动去掉结尾补加的`=`。    
	>>> import base64
	>>> base64.b64encode(b'hello world')
	b'aGVsbG8gd29ybGQ='
	>>> base64.b64decode(b'aGVsbG8gd29ybGQ=')
	b'hello world'

`Base64`编码只是一种通过下标查表获取结果的编码方法，不能用于加密。    

## 摘要算法
Python的`hashlib`模块提供了常见的摘要算法，比如`MD5`，`SHA1`等等。     
摘要算法又称为哈希算法、散列算法，通过一个函数，把任意长度的字符串转换成长度固定的数据串。    
摘要算法就是根据摘要函数对任意长度的数据计算出固定长度的`digest`，可以校验出数据是否被篡改过。    

### MD5
MD5是最常见的摘要算法，速度很快，生成结果是固定的128bit长度的16进制字符串。     
	>>> import hashlib
	>>> md5 = hashlib.md5()
	>>> md5.update('hello world'.encode('utf-8'))
	>>> md5.hexdigest()
	'5eb63bbbe01eeed093cb22bb8f5acdc3'
MD5如果数据内容太长，也可以用多次`update()`，结果是一样的。    
	>>> md5 = hashlib.md5()
	>>> md5.update('hello '.encode('utf-8'))
	>>> md5.update('world'.encode('utf-8'))
	>>> md5.hexdigest()
	'5eb63bbbe01eeed093cb22bb8f5acdc3'

### SHA1
SHA1和MD5调用的方法类似，结果是160bit长度的16进制字符串。     
	>>> sha1 = hashlib.sha1()
	>>> sha1.update('hello world'.encode('utf-8'))
	>>> sha1.hexdigest()
	'2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'

## hmac
通过哈希算法，可以验证一段数据是否有效，就是比对哈希值。    
hmac算法就是在计算哈希的过程中，把key值混入计算，比我们自己加`salt`的哈希算法更标准安全。    
	>>> import hmac
	>>> key = b'salt'
	>>> message = b'hello world'
	>>> h = hmac.new(key, message, digestmod = 'MD5')
	>>> h.hexdigest()
	'406683778d147e1b44bebbe6eeff8091'

## urllib
urllib提供了一系列用于操作URL的功能。    

### Get
urllib的`request`模块可以非常方便的抓取URL内容，也就是发送GET请求到指定的页面，然后返回HTTP响应。    
	>>> import urllib
	>>> url = 'https://baike.baidu.com/item/hello%20world/85501?fr=aladdin'
	>>> from urllib import request
	>>> with request.urlopen(url) as f:
	...     data = f.read()
	...     print('Status: ', f.status, f.reason)
	...     for key, value in f.getheaders():
	...             print('%s: %s' % (key, value))
	...     print('Data: ', data.decode('utf-8'))
	...

返回的内容（网页内容太多，省略显示）：     
	Status:  200 OK
	Content-Type: text/html
	Date: Fri, 08 Jun 2018 09:28:50 GMT
	P3p: CP=" OTI DSP COR IVA OUR IND COM "
	P3p: CP=" OTI DSP COR IVA OUR IND COM "
	Server: Apache
	Set-Cookie: BAIDUID=7F1335CD8449A88889A9738D5452C7AA:FG=1; expires=Sat, 08-Jun-19 09:28:50 GMT; max-age=31536000; path=/; domain=.baidu.com; version=1
	Set-Cookie: BAIDUID=875A6A51DEB2A1CF7E8AAEC19FD7C082:FG=1; expires=Sat, 08-Jun-19 09:28:50 GMT; max-age=31536000; path=/; domain=.baidu.com; version=1
	Vary: Accept-Encoding
	Vary: Accept-Encoding
	Connection: close
	Transfer-Encoding: chunked
	Data:  

如果想要模拟浏览器，需要用到`Request`对象，并且通过往`Reqeust`对象中`add_header()`，就可以把请求伪装成浏览器。    
`add_header()`中的`User-Agent`就是用来标识浏览器的，因此伪装浏览器，这个必须设置。    

### Post
如果要以`Post`发送一个请求，就需要把参数`data`以bytes的形式传入。    

## XML解析
目前XML的解析，主要有DOM和SAX方式。    

### DOM解析
DOM会把整个XML读入内存，解析为树。    
优点：全部解析在内存中，因此可以任意遍历树的节点。    
缺点：读入整个XML内容并且解析，占用内存，解析速度慢。     

### SAX解析
SAX解析是流模式，边读边解析。通常我们使用SAX方式进行XML解析。    
优点：占用内存小，解析快。    
缺点：需要单独处理解析的事件。    
     
Python中用SAX解析XML需要关心的事件：     
1. `start_element`：读取节点头开始的事件
2. `end_element`：读取节点内容的事件
3. `char_data`：读取节点尾的事件

## 练习
1. 用SAX模式解析下面的XML：    
	<?xml version="1.0" encoding="UTF-8"?>
	<section name="SearchInDialog">
		<item value="true" key="SearchInProjects"/>
		<item value="true" key="SearchInAppLibs"/>
		<item value="true" key="SearchInJRE"/>
		<item value="true" key="SearchInSources"/>
	</section>
