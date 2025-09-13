class Solution:
    def isPalindrome(self, s: str) -> bool:


        a=""
        for i in s:
            if i.isalnum()==True:
                a+=f"{i}"
        
        print(a)
        a=a.lower()
        print(a)
        if a==a[::-1]:
            return True
        else:
            return False

        
        