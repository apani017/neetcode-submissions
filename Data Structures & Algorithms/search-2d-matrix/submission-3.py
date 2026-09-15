class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        total = ROWS * COLS

        l, r = 0, total - 1

        while l <= r:
            m = (l+r) // 2
            i = m // COLS
            j = m % COLS
            if matrix[i][j] > target:
                r = m -1
            elif matrix[i][j] < target:
                l = m + 1
            else:
                return True

        return False
