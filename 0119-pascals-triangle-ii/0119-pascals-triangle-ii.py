class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        
        for i in range(1, rowIndex + 1):
            # Calculate the next term using the combination relationship:
            # C(n, k) = C(n, k-1) * (n - k + 1) // k
            row.append(row[-1] * (rowIndex - i + 1) // i)
            
        return row