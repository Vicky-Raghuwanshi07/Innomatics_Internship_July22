from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        binary_1 = []
        for i in range(n+1):
            num_to_bin = bin(i)[2:]
            binary_1.append(num_to_bin.count('1'))
        return binary_1
