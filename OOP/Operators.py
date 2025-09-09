
#COMPARISON OPERATORS
print(1==1)
print(1==2)
print(1>4)
print(6>3)
print(8>=6)
print(6>=6)
print(7<=8)
print(8<=8)

#ASSIGNMENT OPERATORS
a=12
a+=1
print(a)
a=10
a-=1
print(a)
a=4
a*=2
print(a)
a=3
a**=2
print(a)
a=17
a/=4
print(a)

a=17
a%=4
print(a)

a=17
a//=4
print(a)

#unary operand - minus
b=2
print(-b)

#LOGICAL OPERATORS
"""
&& - AND Operator -both conditons have to be tru
|| -OR Operator - one of the conditons have to be true
!- negation operator -negate the expression

MEMBERSHIP OPERATORS CHECK A VALUES IF PART OF A SEQUENCE OR NOT
IN operator- value part of a sqeuqnce or not 
TRUE - IF IT IS A PART
FALSE -IF IT IS NOT

NOT IN -
TRUE -IF VALUE IS NOT PART
FALSE- IF IT IS A PART

"""

X=12
Y=2
A1=[2,4,5,2,13]
print(X in A1)
print(Y in A1)

print(7 not in A1)
print(4 not in A1)

#IDENTITY OPERATORS

print(1 is 1)
print(1 is 2)
print(1 is not 2)
print( 1 is not 1)

#bitwise operator -carry out operation on binary or decimal digits
""" 
& - AND Operation
| - Or Operation
~ - NOT Operation
^ -XOR Operation
