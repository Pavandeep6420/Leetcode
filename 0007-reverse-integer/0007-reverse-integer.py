class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit integer boundaries (-2^31 to 2^31 - 1)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Extract sign and work with absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow/underflow before updating rev
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
                return 0
                
            rev = rev * 10 + digit
            
        return sign * rev