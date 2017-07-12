# def say_hello():
#     print('hello~')
#
# say_hello()
# say_hello()
# 注释多行代码快捷键 command＋／



#global value
original = 50
def change_value():
    global original
    print('original value is',original)

    original = 30
    print('change global value to',original)

change_value()
print('now its value is',original)

#default value
