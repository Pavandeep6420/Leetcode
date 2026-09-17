class Solution:
    def isNumber(self, s: str) -> bool:
        # Flags to track the presence of components
        seen_digit = False
        seen_exponent = False
        seen_dot = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in "+-":
                # A sign is only valid at the very beginning or immediately after an exponent ('e' or 'E')
                if i > 0 and s[i - 1] not in "eE":
                    return False
            elif char in ".":
                # A dot is invalid if we have already seen a dot or an exponent
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif char in "eE":
                # An exponent is valid only if we have seen at least one digit 
                # and haven't seen another exponent yet
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # Reset seen_digit to ensure there are digits *after* the exponent (e.g., "1e" is invalid)
                seen_digit = False
            else:
                # Any other character makes the string invalid
                return False
                
        return seen_digit