# _*_ coding: utf-8 _*_

from math import sqrt

def quadratic(a, b, c):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        factor = (b * b) - (4 * a * c)
        if factor < 0:
            raise ValueError('invalid value of parameter.')
        else:
            return (((0-b) + sqrt(factor)) / (2 * a), ((0 - b) - sqrt(factor)) / (2 * a))
    else:
        raise TypeError('invalid type of parameter.')

if __name__ == '__main__':
    print('x^2 + 2x + 1 = 0, root is [%s]' % str(quadratic(1, 2, 1)))
    print('x^2 - 4 = 0, root is [%s]' % str(quadratic(1, 0, -4)))
    print('ax^2 + bx + c = 0, root is [%s]' % str(quadratic('a', 'b', 'c')))
