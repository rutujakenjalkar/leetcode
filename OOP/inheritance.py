class Parent:
    def __init__(self,parent):
        self.parent=parent

    def display(self):
        print(self.parent)


class Child(Parent):
    def __init__(self, parent,child):
        super().__init__(parent)
        self.child=child

    def Print(self):
        print("the parent class attribut",self.parent)
        print("the child class attribut",self.child)

if __name__=="__main__":
    obj1=Child("sangeeta","rtutuja")
    obj1.display()
    obj1.Print()
   
