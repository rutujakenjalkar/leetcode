class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        dict1={}
        for i in nums:
            if i not in dict1.keys():
                dict1[i]=1
            else:
                dict1[i]+=1

        x=list(dict1.values())
        print(x)
        for j in x:
            if j>=2 :
                return True
                break
        
        return False
        
        