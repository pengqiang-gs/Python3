# _*_ coding: utf-8 _*_

import re

def valid_phone(phone):
    re_phone = re.compile(r'1\d{10}')
    if re_phone.match(phone) is not None:
        return True
    return False

def valid_email(email):
    re_email = re.compile(r'^[a-zA-Z]([0-9a-zA-Z]|\.|\_)+@[0-9a-zA-Z]+.com$')
    if re_email.match(email) is not None:
        return True
    return False

if __name__ == '__main__':
    print('valid phone 13222004532: ', valid_phone('13222004532'))
    print('valid phone 43546423212: ', valid_phone('43546423212'))

    print('valid email chenzhen@126.com: ', valid_email('chenzhen@126.com'))
    print('valid email chenzhen@126.cn: ', valid_email('chenzhen@126.cn'))
    print('valid email chen_zhen@126.com: ', valid_email('chen_zhen@126.com'))
    print('valid email chen.zhen@126.com: ', valid_email('chen.zhen@126.com'))
    print('valid email chen.zhen@sina.com: ', valid_email('chenzhen@sina.com'))
    print('valid email chen-zhen@126.com: ', valid_email('chen-zhen@126.com'))
    print('valid email chen-zhen@126.com: ', valid_email('chen-zhen@126.com'))
    print('valid email chen-zhen@126.company: ', valid_email('chen-zhen@126.company'))
