#-*- coding:utf-8 -*-
class Student(object):
    _score=10
    @property
    #property 装饰器负责把一个方法变成属性调用
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value <0 or value >100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

stu = Student()
stu.score=120