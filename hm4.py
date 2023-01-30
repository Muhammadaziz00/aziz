class A:
    def __init__(self,name):
        self.name = name

        
class B:
    def __init__(self,age):
        self.age = age
class C:
    def a():
        pass


class D:
    def b():
        pass


class Azi(A,B,C,D):
    def __init__(self, name,age) -> None:
        A.__init__(self,name)
        B.__init__(self,age)
    def __str__(self) -> str:
        return f"{self.name}, {self.age}"


a = Azi("Aziz",16)
print(a)
