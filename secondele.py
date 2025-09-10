def secondele(n,arr):

    sum=0
    for i in range(0,len(arr)-2):

        if arr[i]+arr[i+2]==arr[i+1]:
            
            sum+=1
    print(sum)


        

secondele(3,[1,3,2])