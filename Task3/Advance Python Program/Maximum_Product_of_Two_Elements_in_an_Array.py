from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    prod.append((nums[i]-1)*(nums[j]-1))
        return max(prod)
