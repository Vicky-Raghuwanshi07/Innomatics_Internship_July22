class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bit = bin(x^y)[2:]
        return x_bit.count('1')