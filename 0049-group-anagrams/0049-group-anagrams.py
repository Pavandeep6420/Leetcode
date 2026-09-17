from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the characters of the string to use as a canonical key
            sorted_key = ''.join(sorted(s))
            anagram_map[sorted_key].append(s)
            
        return list(anagram_map.values())