#coding=utf-8


def person(age):
    #函数体，函数内容
    if age >0:
        print('这个人的年龄是正常的。')
        return get_name()
    else:
        print('这个人的年龄是不正常的！')

def get_name():
    print('张三')

person(10)

#