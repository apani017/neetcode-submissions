class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)

        for c, p in prerequisites:
            g[c].append(p)

        visiting, visited = set(), set()
        def dfs(node):
            if node in visited:
                return True
            elif node in visiting:
                return False
            visiting.add(node)

            for nei in g[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        