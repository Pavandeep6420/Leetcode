from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        res = []
        
        # We only need to iterate up to word_len because other starting offsets are covered
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            count = 0
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] += 1
                    count += 1
                    
                    # If there are more instances of a word than allowed, shrink the window from the left
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                        count -= 1
                        
                    # If all words match, record the starting index
                    if count == num_words:
                        res.append(left)
                else:
                    # Reset the window if an invalid word is encountered
                    current_count.clear()
                    count = 0
                    left = right
                    
        return res