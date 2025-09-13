# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def etlp(x):
    if x>5:
        return 1
    else:
        return 0
list1=[23,56,7,1]
more=filter(etlp,list1)
print(list(more))

#filter function is used when we apply a function to all values in list and want the values for which the function comes True

def add_4(x):
    return x+4

new_list=map(add_4,list1)
print(list(new_list))

#map function is used to appply function to all values of a list


#THE reduct function is used to call a function on the first 2 values of a then the result on hte next value etc
import functools
def add(x,y):
    return x+y
    
added=list(functools.reduce(add,list1))
print(added)
