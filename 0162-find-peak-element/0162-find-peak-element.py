class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        if len(nums)<=2:
            x=max(nums)
            y=nums.index(x)
            return y
        else:
            while low<=high:

                mid=low+(high-low)//2

                if nums[mid]==max(nums):
                    return mid

                elif max(nums[0:mid])>max(nums[0:mid+1]):
                    high=mid-1

                else:
                    low=mid+1

            return nums.index(max(nums))
