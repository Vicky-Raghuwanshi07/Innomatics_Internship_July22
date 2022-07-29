class Solution:
    def numIdenticalPairs(self, nums) -> int:
        good_pair = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (i<j) and (nums[i]==nums[j]):
                    good_pair +=1
        return good_pair