class Parent():
    def display(self):
        print("this is the parent class method.")

class Child(Parent):
    def display(self):
        print("this is the child class method.")

if __name__=="__main__":
    obj1=Parent()
    obj1.display()
    obj2=Child()
    obj2.display()

        
