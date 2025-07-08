class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        list1=list(set(nums))
        result=[]
        for i in list1:
            if  nums.count(i)==1:
                result.append(i)

        return(result[0])
        