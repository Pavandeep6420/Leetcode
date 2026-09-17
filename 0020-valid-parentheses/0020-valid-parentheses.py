class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # Pop the top element if stack is not available, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapped opening bracket doesn't match the stack's top element
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If stack is empty, all brackets were matched correctly
        return not stack