#CREATION OF TUPLE 
#EMPTY
t1=()
t2=(1,2,3,4,5,6,6)
print(t2[4:])
print(t2[::2])
print(t2[1:4])
t3=(12,34)

#you cannot modify a tuple so no addin operation or delteing operation

#concetenation
print(t2+t1+t3)

#len
print(len(t2))

#mulitplication
print(t3*5)

#maximum
print(max(t2))
print(min(t2))

#convert str to tuple
print(tuple("hello"))

#membership
print(2 in t2)

print(39 not in t2)

#compare two  >,<,>=,<=
print(t1==t2)

#index Checking 

print(t3.index(12))

#count 
print(t2.count(6))

#assignement with tuples
(x1,x2,x3,x4)=(1,2,4,5)
print("x1:",x1,"x2:",x2)

def all(vals):
    x=min(vals)
    y=max(vals)
    return(x,y)

(min_val,max_val)=all((12,4,6,3,2))
print(min_val)
print(max_val)

#zip()-bind together the same indexed elements of two different tuples
print(list(zip((1,2,3,4),("a","b","c","d"))))
