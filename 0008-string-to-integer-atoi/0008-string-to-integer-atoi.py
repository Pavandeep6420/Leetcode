class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Remove leading whitespaces
        s = s.lstrip()
        if not s:
            return 0
        
        # 2. Check for sign
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        # 3. Convert digits and stop at the first non-digit character
        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
        res *= sign
        
        # 4. Handle 32-bit signed integer boundaries (-2^31 to 2^31 - 1)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res