class Solution:
    def fib(self, n: int) -> int:
        fibo=0
        first=1
        second=0
        if n==2:
            return first+second
        elif n==1:
            return 1
        else:
            for i in range(2,n+1):
                print("coming here")
                fibo=first+second
                print(fibo)
                second=first
                print("second",second)
                first=fibo
                print("first",first)

        return fibo
