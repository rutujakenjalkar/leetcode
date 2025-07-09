class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i==target:
                return nums.index(i)
            
            else:
                if target<min(nums):
                        return 0
                elif target>max(nums):
                        return len(nums)
                else:
                    if target<i:
                        return nums.index(i)