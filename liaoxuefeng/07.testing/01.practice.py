# _*_ coding: utf-8 

def factor(number):
    '''
    Calculate 1 * 2 * ... * number

    >>> factor(1)
    1

    >>> factor(-1)
    ?

    >>> factor(5)
    120

    >>> factor(10)
    ?
    '''

    if number < 1:
        raise ValueError('invalid value of input number.')
    elif number == 1:
        return 1
    else:
        return number * factor(number - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
