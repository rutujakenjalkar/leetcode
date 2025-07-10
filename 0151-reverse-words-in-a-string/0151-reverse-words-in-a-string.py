class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        list1=s.split()
        print(list1)
        list2=list1[::-1]
        print(list2)
        s1=' '.join(list2)
        print(s1)
        return s1