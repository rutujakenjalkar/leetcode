class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        list1=[]
        n=len(nums)
        for j in range(n):
            list1.append(0)
        
        print(list1)
        for i in range(n):
            x=(i+k)%n
            print("x:",x)
            print("i:",i)

            temp=nums[i]
            list1[x]=temp

        print(nums)
        for i in range(n):
            nums[i]=0
            nums[i]=list1[i]

        print(nums)