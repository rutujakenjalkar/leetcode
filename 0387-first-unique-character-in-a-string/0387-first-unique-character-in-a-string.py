class Solution:
    def firstUniqChar(self, s: str) -> int:

        dict1={}
        for i in s:
            if i not in dict1.keys():
                dict1[i]=1
            else:
                dict1[i]+=1
        
        
        for x in dict1:
            if dict1[x]==1:
                return s.index(x)
                break
        
        return -1
                

        