class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: 1 step has 1 way, 2 steps have 2 ways
        if n <= 2:
            return n
        
        # Space-optimized Dynamic Programming (Fibonacci pattern)
        # 'a' represents ways to reach step (i-2), 'b' represents ways to reach step (i-1)
        a, b = 1, 2
        
        for _ in range(3, n + 1):
            a, b = b, a + b
            
        return b