class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = []
        for i in range(n):
            result.append(start + (2*i));
        print(result)
        xor = 0
        for i in result:
            xor^=i;
        return xor