class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 0,1,2 ; 3,4,5; 6,7,8
        # 3x3 box 0-0, 0-1, 0-2; 1-0, 1-1, 1-2; 2-0, 2-1; 2-2

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True


        

        