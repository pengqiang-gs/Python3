# _*_ coding: utf-8

class Student(object):
    counter = 0

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

        # 每次创建实例，类的属性：计数器会自增1
        Student.counter = Student.counter + 1

    def name(self, name):
        self.__name = name

    def name(self):
        return self.__name

    def gender(self, gender):
        self.__gender = gender

    def gender(self):
        return self.__gender

    def __str__(self):
        return '[%s, %s]' % (self.__name, self.__gender)

if __name__ == '__main__':
    student1 = Student('Lily', 'Female')
    student2 = Student('Lilei', 'Male')
    student3 = Student('Lucy', 'Female')
    student4 = Student('Jim', 'Male')

    print('there are %d students in the class: ' % Student.counter)
    print(str(student1))
    print(str(student2))
    print(str(student3))
    print(str(student4))
