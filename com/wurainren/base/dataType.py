# -*- coding:utf-8 -*-

#Python内置的一种数据类型是列表：list。
# list是一种有序的集合，可以随时添加和删除其中的元素。

classmates = ['Michael', 'Bob', 'Tracy']
# query 通过下标；切片
print(classmates[0])
print(classmates[-1])
print(classmates[:1])  #===》这里切出来的结果，还是一个list

# count 通过len()函数 获取list元素的个数
print(len(classmates))

# add 通过append()函数，追加元素到末尾；insert()函数 将元素插入指定的位置
classmates.append('Adem')
print(classmates)
classmates.insert(1,'Good')
print(classmates)
classmates[1]='Jack'
print(classmates)

# delete 通过pop()函数，删除list末尾；也可用指定位置删除元素
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)


L =[
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])


#有序列表元组：tuple。
# tuple和list非常类似，但是tuple一旦初始化就不能修改

myClassName = ('Michael', 'Bob', 'Tracy')

t=(1,2)
print(t)
print(t[0])
print(t[1])
print(t[-1])

#list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们