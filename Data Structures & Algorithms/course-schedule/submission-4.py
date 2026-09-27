class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapp = defaultdict(list)
        # print(mapp)

        for c, p in prerequisites:
            mapp[c].append(p)

        
        visit = set()
        def dfs(c):
            if c in visit:
                return False
            if mapp[c] == []:
                return True

            visit.add(c)
            
            for p in mapp[c]:
                if not dfs(p): return False
            visit.remove(c)
            mapp[c] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True