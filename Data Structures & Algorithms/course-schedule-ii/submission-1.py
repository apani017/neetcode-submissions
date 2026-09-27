class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        order = []
        visiting = set()
        visited = set()

        for c, p in prerequisites:
            g[c].append(p)
        

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visiting.add(node)
            
            for nei in g[node]:
                if not dfs(nei):
                    return False
            visited.add(node)
            visiting.remove(node)
            order.append(node)
            return True
            # pass
        

        for i in range(numCourses):
            if not dfs(i):
                return []
        return order