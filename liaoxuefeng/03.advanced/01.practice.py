# _*_ coding: utf-8

def trim(string):
	if string == '':
		return string
	else:
		# trim left
		while string[0] == ' ':
			string = string[1:]

		# trim right
		while string[-1] == ' ':
			string = string[:-1]

	return string

if __name__ == '__main__':
	string = '   hello world   '
	print('before trim: [%s]' % string)
	print('after trim: [%s]' % trim(string))
