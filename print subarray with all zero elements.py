#Print the first element of the main list which has all zero elements
def first_zero(x)->int:
    for i in x:
        sum(i)
        if sum(i)==0:
            return x.index(i)
            break




if __name__=="__main__":
    
 x=[[1,23],[4,5,6],[1,46,76],[0]]
 print(first_zero(x))
