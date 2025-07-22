class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
       string_list=s.split()
       print(string_list)
       if len(string_list)!=len(pattern):
         return False
       else:

         dict1={}
         for i in range(len(string_list)):
            dict1[string_list[i]]=pattern[i]
                
         dict2={}
         for j in range(len(pattern)):
            print(pattern[j])
            print(string_list[j])
            dict2[pattern[j]]=string_list[j]
         print(dict2)
                
         print(dict1)
         
         return list(dict2.values())==list(dict1.keys()) and list(dict1.values())==list(dict2.keys())
