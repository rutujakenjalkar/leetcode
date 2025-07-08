class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        half=n/2
        list1=list(set(nums))
        result=[]
        for i in list1:
            if  nums.count(i)>n/2:
                result.append(i)

        return result[0]