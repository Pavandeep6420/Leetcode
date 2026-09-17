class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        current_line = []
        current_length = 0
        
        for word in words:
            # Check if adding the new word exceeds the maxWidth 
            # (current_length + len(word) + number of words as minimum spaces)
            if current_length + len(word) + len(current_line) > maxWidth:
                # Format the current line
                spaces_to_add = maxWidth - current_length
                num_gaps = len(current_line) - 1
                
                if num_gaps == 0:
                    # If there's only one word in the line, left-justify it
                    res.append(current_line[0] + " " * spaces_to_add)
                else:
                    # Distribute spaces evenly among gaps
                    spaces_per_gap = spaces_to_add // num_gaps
                    extra_spaces = spaces_to_add % num_gaps
                    
                    line_str = ""
                    for i in range(num_gaps):
                        line_str += current_line[i] + " " * (spaces_per_gap + (1 if i < extra_spaces else 0))
                    line_str += current_line[-1]
                    res.append(line_str)
                
                # Reset for the next line
                current_line = []
                current_length = 0
                
            current_line.append(word)
            current_length += len(word)
            
        # Handle the last line (left-justified)
        last_line = " ".join(current_line)
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res