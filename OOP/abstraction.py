from abc import ABC,abstractmethod

class Parent(ABC):

    def __init__(self,name,age):
        self.name=name
        self.age=age

    @abstractmethod
    def display(self):
        pass


class Child(Parent):
    def __init__(self,name,age,city):
        super().__init__(name,age)
        self.city=city

    def display(self):
        print(f"Hi,Iam {self.name} and iam {self.age} years old. I live in {self.city} ")


if __name__=="__main__":
    obj1=Child("rutuja",21,"pune")
    obj1.display()
