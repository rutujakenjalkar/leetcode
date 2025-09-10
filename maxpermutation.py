

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)






def maxpermutation(arr):
    
    vox=["a","e","i","o","u"]
    list1=[]
    for i in range(0,len(arr)):
        s=0
        for x in arr[i]:
            if x not in vox:
                s+=1
        list1.append(s)

    maxi=0
    for i in list1:
        y=factorial(i)
        if y>maxi:
            maxi=y

    print(maxi)

maxpermutation(["hello","ccbc","aaeiou"])


        




