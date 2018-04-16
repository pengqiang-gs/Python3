# _*_ coding: utf-8

def title_string(string):
    return string.title()

def normalize(string_list):
    return list(map(title_string, string_list))

if __name__ == '__main__':
    name_list = ['lily', 'LUCY', 'heLLO', 'WorLD']
    print(normalize(name_list))
