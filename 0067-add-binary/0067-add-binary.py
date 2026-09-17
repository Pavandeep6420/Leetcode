class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        
        # Loop from the rightmost digits to the leftmost digits
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # Calculate the new carry and the current bit to append
            carry = total // 2
            res.append(str(total % 2))
            
        # Reverse the result list since we added digits from right to left, then join into a string
        return "".join(res[::-1])