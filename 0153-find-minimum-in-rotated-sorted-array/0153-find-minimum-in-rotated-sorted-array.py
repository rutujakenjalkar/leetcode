class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        if len(nums)<=2:
            x=min(nums)
            
            return x
        else:
            while low<=high:

                mid=low+(high-low)//2

                if nums[mid+1]<nums[mid]:
                    return nums[mid+1]
                elif nums[mid-1]>nums[mid]:
                    return nums[mid]
                    
                elif nums[-1]>nums[mid]:
                    high=mid-1

                else:
                    low=mid+1

            

        