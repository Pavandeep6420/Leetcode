class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle boundary conditions for 32-bit signed integer overflow
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive numbers using bitwise operations
        a, b = abs(dividend), abs(divisor)
        res = 0
        
        while a >= b:
            temp_divisor, multiple = b, 1
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            a -= temp_divisor
            res += multiple
            
        return -res if negative else res