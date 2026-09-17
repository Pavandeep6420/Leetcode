class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Sort the array of strings
        strs.sort()
        
        # The common prefix of the whole array must be a prefix of 
        # both the first and the last string in the sorted array
        first = strs[0]
        last = strs[-1]
        
        min_len = min(len(first), len(last))
        for i in range(min_len):
            if first[i] != last[i]:
                return first[:i]
                
        return first[:min_len]