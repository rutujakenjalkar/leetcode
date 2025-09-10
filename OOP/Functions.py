#ALL VARIABLES CANNOT BE ACCESSED EVERYWHERE
#scope= the part where the variable is accessible
#lifetime=suration where it is accesible

#global varibles- in the main body of the code can be accessed anywhere
#local varibles present inside the function or classes exist only till the class,function is wroking


s="rutuja"

def show():
    print(s)

show()

#global keyword to declare a varibale inside the function as global

def name():
    global x
    x="rutuja"

#first call the fucntion and then use the global variable
name()
print(x)


#if the global varaibles and local varaibles  names are clashing another local var created with the same name.
var ="outer"
def work(): 
    var="inner"
    print(var)

work()
print(var)

# if global varibale decalred in main as well as inside functn code then changes made once it reflect everywhere
ed="sjdf"
def glow():
    global ed
    ed ="asdf"
    print("ed is:",ed)

glow()
print("outer:",ed)

"""funct1:
        funct2:
            


variables of func1 can be accessed in func2 but outer varibales can be accessed only outside functions .
    """

"you cannot define the local varibles same name as global vaaribale inn that case u have to use the global key word"

#function may or may not return a values
#good practise to use it .
#default value returned by return statetmtn in none used to enter and exit a function
#any code after the return statemnet in the function never gets executed.

#types of argument
"""
1. required argument-def show(str)
2. keyword argumenst-def show(a,b) values assigned to varibles based in name not psoiton
3.default argument - def name(name="anja",age)
4.positional argumnets parameter must be passed postionally 
 def intro(name,age,city)
 eg :intro("rutuja",23,"Pune")
5. To pass variable number of arguments use astrix

#lambds functions are declared with lambda keyword also these are one line functions

"""
sum=lambda x,y:x+y
print(sum(2,3))

power=lambda x:x*2
print(power(3))

"""MODULES:
THESE ARE A COLLECTION OF FUNCTIONS AND VARIABLES DEFINITONS WHICH CAN BE RESUSED MULTIPLT TIMES WHEN REQUIRED (A PYTHON FILE)

To use a module prsent in the current working directory 
import <module name>
module should either be in the same directory or downleded in the python path"""

""" a module can contain large function varibles and deinfitons if you want to use only some them tehn
from <module> import <class>

1. if you want to import multiples classes or varibles
 from <module> import <class1>,<class2>,class3

 to exit from python sys.exit(0) id used denotes succesfule termination
 any other interger denotes abnormal termination

 name of the module is given by __name__

 dir():
 gives list of indentifiers in the mdule ie classes functions varibles,
 to call dir directly use :
 dir()

 to use varible from another module do 
 syntax:
    <module-name>.<variable>

 some modules are already predefined and installed in the python library .

"""

#RECUSRSIVE FUNCTIONS:

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)

print(factorial (4))

def exponential(n,x):
    if (x==0):
        return 1
    else:
        return n*exponential(n,x-1)

print(exponential(2,3))

#fibonnacci series sum of last and second last
def fibonacci(n):
    if n<=2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(0))