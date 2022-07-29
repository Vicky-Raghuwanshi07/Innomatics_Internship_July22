class Solution:
    def smallerNumbersThanCurrent(self, nums):
        count_of_smaller = []
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if (i==j):
                    continue
                elif(nums[i]>nums[j]):
                    counter+=1
            count_of_smaller.append(counter)
        return count_of_smaller