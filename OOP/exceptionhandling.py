"""These appear a lot in coding rounds:

ValueError → wrong data type, e.g., int("abc")

TypeError → invalid operation between types, e.g., "5" + 2

IndexError → accessing invalid index in a list/string

KeyError → missing key in dictionary

ZeroDivisionError → divide by zero

FileNotFoundError → file not found in file handling

ImportError / ModuleNotFoundError → wrong module import

NameError-caused due to a function
SyntaxError"""

#simple exeptions handling

try :
    x=1/0
    print(x)
except ZeroDivisionError:
    print("zero divsion exception caught")


#multple excpetion blocks
try:
    list1=[2,34,1]
    print(list1[6])
except ValueError:
    print("value error caught")
except IndexError:
    print("index error caught")

#multiple exceptions in a single block:
try :
    x=int("frg")
    print(x+["ert"])
    list1=[23,56,7]
    print(list1[7])
except (ValueError,TypeError,IndexError):
    print("both the error caught")

#block wuthout exceptions (else statemnet)
try:
    print(1+2)
except TypeError:
    print("caught")
else:
    print("no error found")

#except block without exception
try:
    print(1/0)
except:
    print("there is an exception in this block")

#RASING EXCEPTION DELIBERTATLERY
'''try:
    raise ValueError
except:
    print("exception was raised")
    #RERaising the exception and not intnd to handle it is done inht ebexcpet block
    raise
'''
#INSTANTIATING EXCEPTIONS

try :
    #instance creation
    raise Exception("HEllo","world")
except Exception as error1:
    #we can see properties of the instance
    print(error1)
    print(type(error1))
    print(error1.args)

#wothout use of argeuments
try :
    raise Exception("ruth")
except Exception as er:
    print("the exception with no arg use")


#invoked functions exception

def wrok(n):
    print(n/0)
try :
    wrok(2)
except  ZeroDivisionError:
    print("the error is coming from a function")


#Finally actions exceuted before leaving the try catch block
'''try:
    print("leaving the try block")
    raise TypeError
finally:
    print("this is before leaving the block")'''


#ASSERTIONS
assert(1>2),"kuch bhi heehe"