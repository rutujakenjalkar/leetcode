def book(n,k,list1):

    sum1=0
    for i in range(0,len(list1)):
        sum1+=list1[i]

    if k>sum1:
        return 0
    else:
        x=sum1//k
        return x

print(book(4,4,[5,7,8,10]))
print(book(3,5,[2,8,6]))
print(book(6,4,[4,4,4,4,4,4]))
print(book(1,3,[2]))