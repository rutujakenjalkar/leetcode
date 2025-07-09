class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        a=-1
        total_length=m+n
        if total_length==1:
            if nums1==[1]:
                 nums1
            else:
                if nums2==[1]:
                    nums1[0]=1
                    nums1
        else:
            for i in range(total_length):
                if nums1[i]==0 and a+1<len(nums2):
                    a+=1
                    nums1[i]=nums2[a]
                    

            nums1.sort()
                
                

        