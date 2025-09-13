class Solution:
    def isValid(self, s: str) -> bool:

        var=True
        stack=[]
        opening=['(','[','{']
        closing=[')',']','}']
        if len(s)==1:
            var=False
        else:
            for i in s:
                if i in opening:
                    stack.append(i)
                else:
                    if i in closing and s.index(i)!=0:
                        if len(stack)!=0:
                            x=stack.pop()
                            if x=='(' and i!=')':
                                var=False
                                break
                            elif x=='[' and i!=']':
                                var=False
                                break
                            elif x=='{' and i!='}':
                                var=False
                                break
                            else:
                                var=True
                        else:
                            var=False
                            break
                    else:
                        var=False  
                        break   
            
            if len(stack)!=0:
                var= False


        return var
        