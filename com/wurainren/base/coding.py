# name = input("name ：")
# age = input("age：")
# job = input("job：")


## 字符串格式化：方式一
# info = '''
# ------------ info {_name} -----------
# name = {_name}
# age = {_age}
# job = {_job}
# --------------------------------
# '''.format(_name = name,
#            _age = age,
#            _job = job)
#
# print(info)


### 字符串格式：方式二
# info = '''
# ------------ info %s -----------
# name = %s
# age =  %s
# job = %s
# --------------------------------
# ''' %(name,name,age,job)
#
# print(info)


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            #raise ValueError('invalid user response')
            raise ValueError("输入错误！")
        print(reminder)


# ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)