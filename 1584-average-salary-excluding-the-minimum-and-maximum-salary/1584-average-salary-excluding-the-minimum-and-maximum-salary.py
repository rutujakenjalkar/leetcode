class Solution:
    def average(self, salary: List[int]) -> float:

        minimum=salary[0]
        maximum=salary[0]
        for i in salary:
            if minimum>i:
                minimum=i
        
        print(minimum)
        for i in salary:
            if maximum<i:
                maximum=i
        
        print(maximum)

        x=len(salary)-2
        print(x)

        total=0
        for i in salary :
            if i!=minimum and i!=maximum:
                total+=i
        
        print(total)
        return total/x
        