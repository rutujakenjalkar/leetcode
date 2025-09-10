def picnic(n,arr):

    odd_id=0
    even_id=0
    for i in range(0,len(arr)):
        if arr[i]%2==0:
            even_id+=1
        else:
            odd_id+=1
    
    if odd_id>even_id:
        return even_id*2
    elif even_id>odd_id:
        return odd_id*2
    else:
        return even_id*2


print(picnic(6,[1,2,4,5,7,8]))
print(picnic(5,[1,3,5,7,8]))
            