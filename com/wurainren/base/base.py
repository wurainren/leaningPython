#for 循环

# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + x
# print(sum)


# list(range(5))


# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# while 循环

# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)


#请利用循环依次对list中的每个名字打印出Hello, xxx!：
#L = ['Bart', 'Lisa', 'Adam']
'''L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print ('Hello，',i,'!')
'''



#break
'''n=1
while n<=100:
    if n>10:
        break
    print(n)
    n=n+1
print('END')  ''' 

#continue
'''n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n) '''



# dict字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
d['Adam'] =78
print(d['Adam'])
#print(d['Thomas'])

# 判断字典中是否存在某key，使用in关键字；也可以使用get方法，不存在返回None，或自己指定的value
print('Thomas' in d)
print(d.get('Thomas')) #None
print(d.get('Thomas',-1)) #-1


#删除key pop(key)方法
print('删除之前：',d)
d.pop('Bob')
print('删除之后：',d)

'''
请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。

而list相反：

    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。

所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，
正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
'''


# set
s = set([1,1,2,2,3,3])
print('添加之前：',s)        #{1，2，3}
s.add(4)
print('添加之后：',s)

s.remove(4)
print('进行删除：',s)

s1 = set([1, 2, 3])
s2 = set([2,3,4])
print(s1&s2)                #并集
print(s1|s2)                #交集

#set和dict的唯一区别仅在于没有存储对应的value，
# 但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”



#str是不变对象，而list是可变对象。

#1.可变 list
# a=['c','b','a']
# a.sort()
# print(a)

#2.不可变 str
a='abc'
a.replace('a','A')
print(a)


a1 = 'abc'
b1 = a1.replace('a','A')
print(b1)




#-------------------------------------------------------------------------

#函数

print(abs(100))  #100
print(abs(-10))  #10
print(abs(12.34))#12.34
#print(abs(1,2))  #TypeError: abs() takes exactly one argument (2 given)

#数据转换
str='10'
print(str,type(str))
print(int(str),type(int(str)))


#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
#a = abs # 变量c指向abs函数，报错
#a(-1)   # 所以也可以通过c调用abs函数
# 在控制台可以，在py文件中不行
# >>> a=abs
# >>> a(-1)
# 1


n1 = 255
n2 = 1000

#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
print(hex(n1))
print(hex(n2))


#定义函数 
# def关键字 mybas函数名 x入参 return 返回值，默认返回None
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None

def myabs(x):
    if(x>0):
        return x
    else:
        return -x

print(myabs(-555))


#参数类型：
# 1.位置参数
def power(x):
    return x * x
print(power(5)) #25

def power1(x,n):
    s=1
    while n>0:
        n=n-1 #做递减用
        s=s*x
    return s
print(power1(5,2)) #25

# 2.默认参数
# 可以设置只传入一个参数x，n可以不用传入，默认为2
# 设置默认参数时，有几点要注意：
#   一是必选参数在前，默认参数在后，否则Python的解释器会报错；
#   二是如何设置默认参数。当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现
# 默认参数必须指向不变对象
def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power2(5)) #25

