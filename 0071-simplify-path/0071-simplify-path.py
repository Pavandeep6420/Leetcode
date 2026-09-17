class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # Split the path by '/' to examine each component individually
        components = path.split("/")
        
        for comp in components:
            if comp == "..":
                # Go up to the parent directory if the stack has elements
                if stack:
                    stack.pop()
            elif comp and comp != ".":
                # If it's a valid directory name or any sequence like '...', push it
                stack.append(comp)
                
        # Reconstruct the canonical path by joining stack elements with '/'
        return "/" + "/".join(stack)