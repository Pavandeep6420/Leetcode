class Solution:
    def grayCode(self, n: int) -> list[int]:
        # Generate Gray code using the binary-to-Gray formula: i ^ (i >> 1)
        return [i ^ (i >> 1) for i in range(1 << n)]