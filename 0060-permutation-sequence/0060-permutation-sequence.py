import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1  # Convert k to 0-indexed
        res = []
        
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            res.append(numbers.pop(index))
            k %= fact
            
        return "".join(res)