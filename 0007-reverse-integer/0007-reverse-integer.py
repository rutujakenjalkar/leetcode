class Solution:
    def reverse(self, x: int) -> int:
        
        list1=[]
        numbers=str(x)
        for i in numbers:
            if i !="-":
              list1.append(int(i))

        print(list1)

        final=0
        for i in range(len(list1)):
            a=list1[i]
            b=(10**i)*a
            print("i:",i)
            print("b:",b)
            final+=b


        if ((-2)**31)<final<=(2**31)-1 :
            if x<0:
                return -final
            else:
                return final

        return 0
        

        
        

       