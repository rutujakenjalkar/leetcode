
#if statement

x=10
if (x==10):
    print("the number is 10.")

#if -else statement
a=12
if (a==10):
    print("this is 10.")
else:
    print("the number is something else..")


#nested if -if one "if" block is placed inside another
if (a==12):
    if (x==10):
        print("a is 12 x is 10.")

    
#if-elif-else
""" between if and else multiple elifs are possible ,elif and else are optional"""

a=9

if a==1:
    print(1)
elif a==2:
    print(2)
elif a==3:
    print(3)
else:
    print("not 1,2,3")


#while loop , executes until a given condition is satisfied once it becomes false then, it stops 
""" first the condition is checked after which the loop goes on"""

x=0
while(x<5):
    x+=1

print(x)

#for looop is also known as definite loop as we know the times it will repeat.repriton over number or set of values
x=[1,23,4,5]
for i in x :
    print(i)

for i in range(0,5):
    print(i)

"""range -built in function to iterate over a set of values"""

"""break statment to come out of nearest possible loop"""
for i in x:
    print(i)
    if i>10:
        break
print("out of loop")

""" continue -loop iteration skipped on a condition"""
for i in range(0,5):
    if x==1:
        continue
    print(i)

"""pass statement a used for a command that does nothing"""

for i in range(0,3):
    pass
    print("passs")
        
""" (0,3)===> 2values"""
""" range(0,3)===> 0,1,2"""

