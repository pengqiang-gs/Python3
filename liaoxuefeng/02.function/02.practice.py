# _*_ coding: utf-8 _*_

def move(N, A, B, C):
    if isinstance(N, (int, float)):
        if N == 1:
            print(A, ' --> ', C)
        else:
            move(N-1, A, C, B)
            move(1, A, B, C)
            move(N-1, B, A, C)

    else:
        raise TypeError('invalid type of parameter.')

if __name__ == '__main__':
    number = input('请输入汉诺塔A上的盘子数目：')
    move(int(number), 'A', 'B', 'C')
