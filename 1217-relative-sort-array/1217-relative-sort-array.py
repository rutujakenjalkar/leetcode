class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        dict1={}
        for i in arr1:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        
        output_list=[]
        print(dict1)

        for i in arr2:
            if i in dict1:
               for j in range(0,dict1[i]):
                    output_list.append(i)

        list2=[]
        for i in arr1:
            if i not in arr2:
                list2.append(i)

        list2=sorted(list2)
        print(list2)

        output_list=output_list+list2
        return output_list




        
        