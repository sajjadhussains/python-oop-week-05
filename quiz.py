# class Test:
#     def __init__(self):
#         self.x = 0
# class Derived_Test(Test):
#     def __init__(self):
#         Test.__init__(self)
#         self.y = 1
# def main():
#     b = Derived_Test()
#     print(b.x,b.y)
# main()
# from abc import ABC, abstractmethod
# class AbstractClass(ABC):
#      @abstractmethod
#      def some_method():
#         pass
# ac = AbstractClass()

# print(ac)
# try:
#     if '1' != 1:
#         raise "someError"
#     else:
#         print("someError has not occurred")
# except "someError":
#     print ("someError has occurred")
# class A:
#     def __str__(self):
#         return '1'
# class B(A):
#     def __init__(self):
#         super().__init__()
# class C(B):
#     def __init__(self):
#         super().__init__()
# def main():
#     obj1 = B()
#     obj2 = A()
#     obj3 = C()
#     print(obj1, obj2,obj3)
# main()
# class A:
#     def __init__(self):
#         self.multiply(15)
#     def multiply(self, i):
#         self.i = 4 * i;
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print(self.i)
 
#     def multiply(self, i):
#         self.i = 2 * i;
# obj = B()
# def mk(x):
#     def mk1():
#         print("Decorated")
#         x()
#     return mk1
# def mk2():
#     print("Ordinary")
# p = mk(mk2)
# p()
# CODE 1
#   @f
# def f1():
#         print(“Hello”)
# CODE 2
#   def f1():
#          print(“Hello”)
# f1 = f(f1)
class A:
    @staticmethod
    def a(x):
        print(x)
A.a(100)
