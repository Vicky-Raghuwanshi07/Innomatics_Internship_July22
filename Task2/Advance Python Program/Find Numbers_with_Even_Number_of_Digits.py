class Solution:
    def findNumbers(self, nums) -> int:
        even_digits = 0
        for i in nums:
            if len(str(i))%2==0:
                even_digits+=1
        return even_digits