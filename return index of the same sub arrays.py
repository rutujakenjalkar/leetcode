#Print the first element of the main list which has all zero elements
def equal_list(x)->tuple:
    a=0
    b=0
    n=len(x)
    for i in range(n):
       for j in range(n):
          if x[i]==x[j]:
             a=i
             b=j
             break

    
    if a!=0 and b!=0:
       return(a,b)
    else:
       return(0,0)

 

if __name__=="__main__":
    
 x=[[1,23],[1,23],[1,46,76],[4,5,6]]
 print(equal_list(x))
