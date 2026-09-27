class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        
        def addCell(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == -1 or
                (r, c) in visit):
                return

            visit.add((r, c))
            q.append([r, c])


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        d = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = d
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r, c-1)
            d += 1