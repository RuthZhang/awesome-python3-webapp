#-*- coding:utf-8 -*-
import pymysql
import time,uuid
from types import MethodType
# class Hello(object):
#     def hello(self,name="world"):
#         print('hello,%s'%name)
# h=Hello()
# h.hello()
# print(type(Hello))
# print(type(h))
#
# print('%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex))

class Student(object):
    count=0
    def __init__(self,name,score,age):
        self.__name=name
        self.__score=score
        self.age = age
    def print_score(self):
        print('%s,%s'%(self.name,self.score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_score(self,score):
        if(0 <= score <=100):
            self.__score = score
        else:
            raise ValueError('bad score')

def set_age(self,age):
    self.age = age

stu = Student("zhang",100,age=2.5)
stu.set_score(99)
print(hasattr(stu,'age'))

print(getattr(stu,'age'))
print(getattr(stu,'count'))
stu.set_age = MethodType (set_age,stu)
stu.set_age(25)
print(stu.age)

class Person(object):
    __slots__ = ('name','age')
    def __init__(self,name,age):
        self.name = name;
        self.age=age

s= Person("zhang",32)
s.sex='F'
# bart=Student("Bart Simpson" ,59)
# #print(bart.name)
# print_score(bart)
# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.age=10
# print(bart.age)
# print(lisa.score)

# c=pymysql.connect('127.0.0.1','root','root','test')
# x=c.cursor(pymysql.cursors.DictCursor)
# print(x.execute('select * from user'))
# print(x.fetchall())
# def power(x,n=2):
#     s=1
#     while n>0:
#         n=n-1
#         s=s*x
#     return s
#

# print(power(5,2))
# print(power(100))
#
# def enroll(name,gen,age=6,city='beijing'):
#     print('name:',name)
#     print('gender:',gen)
#     print('age:',age)
#     print('city:',city)
#
# enroll('Sara','F')
#
# def calc(*numbers):
#     sum=0
#     for n in numbers:
#         sum=sum + n*n
#     return sum
#
# print(calc(1,2))
# print(calc())
#
# nums=[1,2,3]
# print(calc(*nums))
#
# def person(name,age,**kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
# person('Michael', 30)