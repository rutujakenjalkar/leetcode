class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero=[]
        zero=[]
        for i in range(0,len(nums)):
            if nums[i]==0:
                zero.append(0)
            else:
                non_zero.append(nums[i])
        
        print(non_zero)
        print(zero)
        nums[:]=[]
        for i in non_zero:
            nums.append(i)
        
        for i in zero:
            nums.append(i)
        