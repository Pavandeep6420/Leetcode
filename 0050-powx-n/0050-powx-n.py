class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Helper function to perform binary exponentiation for non-negative powers
        def helper(base: float, exponent: int) -> float:
            if exponent == 0:
                return 1.0
            if base == 0:
                return 0.0
            
            res = helper(base * base, exponent // 2)
            return res * base if exponent % 2 == 1 else res

        # Handle negative exponents by turning n positive and using reciprocal
        if n < 0:
            return 1.0 / helper(x, -n)
        return helper(x, n)