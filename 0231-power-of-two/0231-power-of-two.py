class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n==1:
            return True
        else:
            x=1
            while(n>x):
                x*=2
            
            if x==n:
                return True
            else:
                return False
            

        