class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)

        for c, p in prerequisites:
            pre[c].append(p)

        output = []
        visit, cycle = set(), set()

        def dfs(c):
            if c in cycle:
                return False

            if c in visit:
                return True

            cycle.add(c)

            for p in pre[c]:
                if dfs(p) == False:
                    return False

            cycle.remove(c)
            visit.add(c)
            output.append(c)

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output