# -*- coding:utf-8 -*-
"""
@author:YCW
@file:zoo.py
@time:2020/11/15 16:36
"""
"""
背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。
具体要求：
定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。

"""

from abc import ABCMeta, abstractmethod


class Zoo(object):

    def __init__(self, name):
        self._name = name

    def __getattr__(self, item):
        try:
            self.__getattribute__(item)
        except AttributeError:
            return None
        return self.__getattribute__(item)

    @property
    def name(self):
        return self._name

    def add_animal(self, animal):
        if not self.__getattr__(animal.__class__.__name__):
            self.__setattr__(animal.__class__.__name__, animal)


class Animals(metaclass=ABCMeta):

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def character(self):
        pass

    @abstractmethod
    def is_fierce(self):
        pass


class Cat(Animals):

    call = '喵喵喵'

    def __init__(self, name, type, size, character):
        self._name = name
        self._type = type
        self._size = size
        self._character = character

    def name(self):
        return self._name

    def type(self):
        if self._type == '食肉':
            return True
        return False

    def size(self):
        if self._size == '小':
            return 1
        elif self._size == '中等':
            return 2
        elif self._size == '大':
            return 3

    def character(self):
        if self._character == '凶猛':
            return True
        return False

    def is_fierce(self):
        if self.size() >= 2 and self.type() and self.character():
            return True
        return False

    def is_pet(self):
        if self.character():
            return False
        return True


class Dog(Animals):

    call = '汪汪汪'

    def __init__(self, name, type, size, character):
        self._name = name
        self._type = type
        self._size = size
        self._character = character

    def name(self):
        return self._name

    def type(self):
        if self._type == '食肉':
            return True
        return False

    def size(self):
        if self._size == '小':
            return 1
        elif self._size == '中等':
            return 2
        elif self._size == '大':
            return 3

    def character(self):
        if self._character == '凶猛':
            return True
        return False

    def is_fierce(self):
        if self.size() >= 2 and self.type() and self.character():
            return True
        return False

    def is_pet(self):
        if self.character():
            return False
        return True


if __name__ == '__main__':

    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    dog1 = Dog('小狗狗 2', '食肉', '小', '温顺')
    dog2 = Dog('大狼狗 3', '食肉', '大', '凶猛')
    print(cat1.is_fierce())
    print(cat1.is_pet())
    print(dog1.is_fierce())
    print(dog1.is_pet())
    print(dog2.is_fierce())
    print(dog2.is_pet())
    # 增加一只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat1)
    z.add_animal(dog1)
    z.add_animal(dog2)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)