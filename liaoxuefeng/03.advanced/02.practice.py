# _*_ coding: utf-8 

def fibnacci(count):
	counter, a, b = 0, 0, 1
	while counter < count:
		yield b
		a, b = b, a + b
		counter = counter + 1

def triangle(count):
	counter, line = 0, [1]
	while counter < count:
		yield line
		pre_line = []
		for item in line:
			pre_line.append(item)
		index = 0
		while index < len(pre_line) - 1:
			line[index+1] = pre_line[index] + pre_line[index+1]
			index = index + 1
		line.append(1)
		counter = counter + 1

if __name__ == '__main__':
	# test fibnacci
	count = int(input('请输入需要的斐波那契数列个数：'))
	for item in fibnacci(count):
		print(item, ' ')
	
	count = int(input('请输入需要的杨辉三角行数：'))
	for item in triangle(count):
		print(item)
