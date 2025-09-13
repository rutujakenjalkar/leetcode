class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts={}
        dictt={}
        for i in s :
            if i not in dicts:
                dicts[i]=1
            else:
                dicts[i]+=1
        

        for i in t :
            if i not in dictt:
                dictt[i]=1
            else:
                dictt[i]+=1


        print(dicts)
        print(dictt)

        x=dicts.keys()
        y=dictt.keys()

        if x!=y:
            return False
        else:
            for i in x:
                if dicts[i]!=dictt[i]:
                    return False
                    break
        
        return True
