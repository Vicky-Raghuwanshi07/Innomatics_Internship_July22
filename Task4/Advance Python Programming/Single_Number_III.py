from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)==len(set(nums)):
            return nums
        else:
            non_repeat_num = []
            for i in nums:
                if nums.count(i)==1:
                    non_repeat_num.append(i)
            return non_repeat_num