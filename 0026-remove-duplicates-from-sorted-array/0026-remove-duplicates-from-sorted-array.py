class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        list1=set(nums)
        list2=list(list1)
        for i in list2:
            while (nums.count(i)>1):
                nums.remove(i)


        
        return(len(nums))