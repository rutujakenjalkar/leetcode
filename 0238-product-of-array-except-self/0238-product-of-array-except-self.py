class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       n=len(nums)
       list1=[1]*n
       print(list1)
       for i in range(1,n):
          list1[i]=list1[i-1]*nums[i-1]

       print(list1)
       right=nums[-1]
       for i in range(n-2,-1,-1):
         list1[i]*=right
         right*=nums[i]

       return list1  