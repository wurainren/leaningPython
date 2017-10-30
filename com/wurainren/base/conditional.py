# if elif else 

age = 15

if(age>=18):
    print("成年人！")
else:
    print("小屁孩！")
#---------------------------------------
if age<18:
    print("小屁孩！")
else:
    print("大人！")
#---------------------------------------
if age >= 18:
    print('adult')
elif age >= 6:          # <==> else if
    print('teenager')
else:
    print('kid')


# birth = int(input('birth: '))    #input函数 中得到的数据都是字符型的，使用int进行转型
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')


#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
height=1.75
weight=80.5

BMI=80.5/1.75**2
print(BMI)
if BMI<18.5:
    print("过轻")
elif 25>BMI>=18.5:
    print("正常")
elif 28>BMI>=25:
    print("过重")
elif 32>BMI>=28:
    print("肥胖")
elif BMI>=32:
    print("严重肥胖")        
