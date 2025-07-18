class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        if digits[n-1]!=9:
            digits[n-1]+=1

        else:
            if sum(digits)%9==0 and digits.count(9)==n:
                
                digits.append(0)
                for x in range(len(digits)):
                     if x==0:
                            digits[x]=1
                     else:
                            digits[x]=0
                    
            else:
                print("it is here")
                x=n-1
                number=0
                list1=[]
                for i in range(n):
                    a=digits[i]*(10**x)
                    number+=a
                    x-=1
                number+=1
                print(number)

                y=n-1
                for i in range(n):
                    b=number//(10**y)
                    number-=((10**y)*b)
                    print(b)
                    list1.append(b)
                    y-=1
                    print(list1)
                return list1

                    
                

        return digits