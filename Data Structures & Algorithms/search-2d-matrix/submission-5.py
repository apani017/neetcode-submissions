class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        t = rows * cols

        l, r = 0, t-1

        while l <= r:
            m = (l + r) // 2
            i = m // cols
            j = m % cols
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                l = m + 1
            else:
                r = m - 1
        return False