class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            if x<10:
                return True 
            else:
                a=str(x)
                b=a[::-1]
                if a==b:
                    return True 
                else:
                    return False

        else:
            return False
        