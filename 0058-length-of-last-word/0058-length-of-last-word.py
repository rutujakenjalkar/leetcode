class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        x=-1
        
        s=s.rstrip()
        print(s)
        while x >= -len(s) and s[x] != " ":
                print(s[x])
                count+=1
                x-=1

        
        

        return count