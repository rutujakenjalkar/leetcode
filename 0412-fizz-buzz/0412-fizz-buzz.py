class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        out=[]
        for i in range(1,n+1):
            if  i%3==0 and i%5!=0:
                out.append("Fizz")
            elif i%5==0 and i%3!=0:
                out.append("Buzz")
            elif i%3==0 and i%5==0:
                out.append("FizzBuzz")
            else:
                out.append(f"{i}")

        return out

        