import math


class Class0001:

    def __init__(self, var1, var2):
        self.data0001 = math.sqrt(var1)
        self.data0002 = math.sqrt(var2)

    def use_method(self):
        print(self.data0001)

    def set_data1(self, var1):
        self.data0001 = var1

    # class method는 상속을 했다하더라도 해당 클래스(Circle)에만 영향을 미침
    @classmethod
    def class_method_example(cls, name):
        cls.name = name

    # static method는 상속한 곳에서 적용을 시켜도, 부모 클래스까지 영향을 미침
    @staticmethod
    def static_method_example(name):
        Class0001.data0001 = name
