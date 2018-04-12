# _*_ coding: utf-8 _*_

def bmi(height, weight):
    rate = weight / (height * height)
    if rate < 18.5:
        return '过轻'
    elif rate >= 18.5 and rate < 25:
        return '正常'
    elif rate >= 25 and rate < 28:
        return '过重'
    elif rate >= 28 and rate < 32:
        return '肥胖'
    else:
        return '过于肥胖'

if __name__ == '__main__':
    height = input('请输出身高：')
    weight = input('请输出体重：')

    try:
        print('身高：%s m，体重：%s kg， 结论：%s' % 
                (height, weight, bmi(float(height), float(weight))))
    except:
        print('输入的参数有误，请检查。')

