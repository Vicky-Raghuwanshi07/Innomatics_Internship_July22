class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod,s =1,0
        for i in str(n):
            prod *= int(i)
            s+=int(i)
        return (prod-s)