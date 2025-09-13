class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        r=len(nums)

        max_list=[]
        while len(nums)!=0:
            x=max(nums)
            if x not in max_list:
                max_list.append(x)
            else:
                nums.remove(x)
            
        print(max_list)

        if len(max_list)<3:
            return max(max_list)
        else:
            return max_list[2]


        