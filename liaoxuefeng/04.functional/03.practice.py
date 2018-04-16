# _*_ coding: utf-8

def is_palindrome(number):
    if not isinstance(number, int):
        raise TypeError('invalid integer number.')

    number_string = str(number)
    number_length = len(number_string)
    for i in range(0, number_length):
        if number_string[i] != number_string[number_length - i - 1]:
            return False
    return True

def palindrome(number_list):
    return list(filter(is_palindrome, number_list))

if __name__ == '__main__':
    number_list = [1, 12, 121, 123, 1232, 1321, 12321]
    print('original list: ', number_list)
    print('palindrome list: ', palindrome(number_list))
