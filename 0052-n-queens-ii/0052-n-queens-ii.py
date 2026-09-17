class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        positive_diag = set()  # (r + c)
        negative_diag = set()  # (r - c)

        count = 0

        def backtrack(r):
            nonlocal count
            if r == n:
                count += 1
                return

            for c in range(n):
                if c in col or (r + c) in positive_diag or (r - c) in negative_diag:
                    continue

                col.add(c)
                positive_diag.add(r + c)
                negative_diag.add(r - c)

                backtrack(r + 1)

                col.remove(c)
                positive_diag.remove(r + c)
                negative_diag.remove(r - c)

        backtrack(0)
        return count