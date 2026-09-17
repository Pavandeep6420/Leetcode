from functools import lru_cache

class Solution:
    @lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        # Base case: if strings are identical, they are scrambles
        if s1 == s2:
            return True
            
        # Quick prune: if character counts don't match, they cannot be scrambles
        if sorted(s1) != sorted(s2):
            return False
            
        n = len(s1)
        
        # Try all possible split points
        for i in range(1, n):
            # Case 1: No swap of the two parts
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])):
                return True
                
            # Case 2: Swap of the two parts
            if (self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i])):
                return True
                
        return False