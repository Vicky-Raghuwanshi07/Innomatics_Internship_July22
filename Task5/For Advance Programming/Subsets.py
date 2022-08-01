from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for i in nums:
            subsets += [lst + [i] for lst in subsets]
        return subsets