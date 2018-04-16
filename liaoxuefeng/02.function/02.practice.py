# _*_ coding: utf-8 _*_

counter = 0
def move(disk_number, piller_1, piller_2):
	global counter
	counter += 1
	print('第%d次移动：把%d号盘子从柱子%s移动到柱子%s' % 
			(counter, disk_number, piller_1, piller_2))

def hanoi_tower(N, A, B, C):
	if isinstance(N, (int, float)):
		if N == 1:
			move(1, A, C)
		else:
			# move N-1 disks to piller B which based piller A
			hanoi_tower(N-1, A, C, B)
			
			# move left disk to piller C
			move(N, A, C)
			
			# move N-1 disks to piller C which based piller B
			hanoi_tower(N-1, B, A, C)
	else:
		raise TypeError('invalid type of parameter.')

if __name__ == '__main__':
	number = int(input('请输入汉诺塔A上的盘子数目：'))
	hanoi_tower(number, 'A', 'B', 'C')
