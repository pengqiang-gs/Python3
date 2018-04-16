# _*_ coding: utf-8

def counter_generator():
    counter_number = 0
    def counter():
        # 这地方需要修改本函数外部的局部变量，需要声明为nonlocal
        nonlocal counter_number
        counter_number = counter_number + 1
        return counter_number
    return counter

if __name__ == '__main__':
    counter = counter_generator()
    print(counter(), counter(), counter())

