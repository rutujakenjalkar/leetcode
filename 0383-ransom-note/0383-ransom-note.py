class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = {}
        for i in magazine:
            if i not in dict1:
                dict1[i] = magazine.count(i)

        print(dict1)

        for i in ransomNote:
            if i in magazine:
                if dict1.get(i)>0:
                    dict1[i]=dict1[i]-1
                else:
                    return False
                    break
            else:
                return False
                break

        return True