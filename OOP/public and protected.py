
class Student:
       _branch="pune"  #class variable


       #CONSTRUCTOR TO INTIALIZE OBJECT (intance variable)
       def __init__(self,name,rollno):
             self.name=name
             self.rollno=rollno

        
class Girls(Student):
      
      def display_name(self):
            print(self._branch)
    







#THE MAIN FUNCTION
if __name__=="__main__":
    print("OOP")
    obj1=Student("RUTUJA",100)
    print(obj1._branch)
    print(obj1.name)
    print(obj1.rollno)
    obj2=Girls("kedar",123)
    obj2.display_name()
