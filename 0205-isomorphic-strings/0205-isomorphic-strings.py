class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=len(s)
        b=len(t)
        if a!=b:
            return False
        else:
           dict1={}
           dict2={}
           for i in range(a):
              dict1[s[i]]=t[i]

           print(dict1)

           for i in range(b):
             dict2[t[i]]=s[i]

           print(dict2)

           return list(dict1.keys())==list(dict2.values())
