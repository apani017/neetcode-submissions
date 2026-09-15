class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        print(f"ROWS: {ROWS}, COLS: {COLS}")
        
        total = ROWS*COLS
        l, r = 0, total-1

        while l<=r:
            m = (l+r) // 2
            i = m // COLS
            j = m % COLS


            mid = matrix[i][j]
            if mid > target:
                r-=1
            elif mid < target:
                l+=1
            elif mid == target:
                return True
        return False