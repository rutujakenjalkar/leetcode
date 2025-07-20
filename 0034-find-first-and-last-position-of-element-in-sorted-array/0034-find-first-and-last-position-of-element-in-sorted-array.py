class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        left=-1
        right=-1

        while low<=high:

            mid=low+(high-low)//2

            if nums[mid]==target:
                left=mid
                right=mid

                while(left-1>=0 and nums[left-1]==target):
                    left-=1


                while(right+1<len(nums) and nums[right+1]==target):
                    right+=1
                
                break

            elif nums[mid]>target:
                high=mid-1
            
            else:
                low=mid+1

        return left,right

        