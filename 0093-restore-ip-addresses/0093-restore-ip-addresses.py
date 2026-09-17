class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        
        def backtrack(start: int, path: list[str]):
            # If we already have 4 segments
            if len(path) == 4:
                # If we've used up the entire string, it's a valid IP
                if start == len(s):
                    res.append(".".join(path))
                return
            
            # Try segment lengths of 1, 2, and 3
            for length in range(1, 4):
                if start + length > len(s):
                    break
                segment = s[start:start + length]
                
                # Validation rules:
                # 1. No leading zeros for numbers with more than one digit (e.g., "01" is invalid, but "0" is valid)
                # 2. Integer value must be between 0 and 255 inclusive
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue
                    
                backtrack(start + length, path + [segment])
                
        backtrack(0, [])
        return res