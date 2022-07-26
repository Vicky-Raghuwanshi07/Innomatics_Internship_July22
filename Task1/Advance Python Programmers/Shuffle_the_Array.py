class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        end = n
        for i in range(n):
            result.append(nums[i])
            result.append(nums[end])
            end+=1
        return result
