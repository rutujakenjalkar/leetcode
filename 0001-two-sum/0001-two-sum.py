class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        output=[]
        for i in range(n):
            for j in range(n):
                if nums[i]!=nums[j] :
                    if nums[i]+nums[j]==target and output.count(nums[i])==0 and output.count(nums[j])==0 :
                        output.append(i)
                        output.append(j)
                else :
                     if i!=j:
                        if nums[i]+nums[j]==target and output.count(nums[i])==0 and output.count(nums[j])==0 :
                            output.append(i)
                            output.append(j)

        for a in output:
            if output.count(a)>1 :
                output.remove(a)   

        return output


