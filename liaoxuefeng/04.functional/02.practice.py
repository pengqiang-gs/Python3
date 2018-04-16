# _*_ coding: utf-8

from functools import reduce

def char_2_num(char):
    digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
            '7': 7, '8': 8, '9': 9}
    if char not in digit:
        raise TypeError('invalid char element.')

    return digit[char]

def integer(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return (x * 10) + y
    else:
        raise TypeError('invalid integer element.')

decimal_rate = 1
def decimal(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        global decimal_rate
        decimal_rate =decimal_rate * 10
        return x + (y / decimal_rate)
    else:
        raise TypeError('invalid decimal element.')

def string_2_float(string):
    string_list = string.split('.')
    if len(string_list) > 2 :
        raise TypeError('invalid float string.')
    elif len(string_list) <= 0:
        return 0.0
    else:
        integer_string = string.split('.')[0]
        if len(integer_string) <= 0:
            integer_string = '0'
        if len(string_list) == 2:
            decimal_string = '0' + string.split('.')[1]
            if len(decimal_string) <= 0:
                decimal_string = '0'

    return reduce(integer, map(char_2_num, integer_string)) + \
            reduce(decimal, map(char_2_num, decimal_string))

if __name__ == '__main__':
    string = '123.45'
    print('float string: ', string)
    print('string float: ', string_2_float(string))
