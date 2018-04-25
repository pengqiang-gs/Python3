# _*_ coding: utf-8

class Screen(object):

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, height):
		if not isinstance(height, int):
			raise TypeError('invalid type of screen height.')

		if height > 2048 or height < 0:
			raise ValueError('invalid value of screen height')

		self.__height = height

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, width):
		if not isinstance(width, int):
			raise TypeError('invalid type of screen width.')

		if width > 2048 or width < 0:
			raise ValueError('invalid value of screen width.')

		self.__width = width

	@property
	def resolution(self):
		return self.__height * self.__width

if __name__ == '__main__':
	screen = Screen()
	
	height = int(input('input screen height: '))
	screen.height = height

	width = int(input('input screen width: '))
	screen.width = width

	print('screen information: ')
	print('height: ', screen.height)
	print('width: ', screen.width)
	print('resolution: ', screen.resolution)
