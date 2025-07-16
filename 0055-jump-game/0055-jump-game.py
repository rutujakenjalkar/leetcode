class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if n <= 1:
            return True

        maxReach = 0

        for i in range(n):
            if i > maxReach:
                return False  # we can't reach this point
            maxReach = max(maxReach, i + nums[i])

        return True
