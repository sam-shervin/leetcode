from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 -> not visited
        # 1 -> visiting
        # 2 -> no cycle

        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        state = [0]*numCourses
        def dfs(node):
            if state[node] == 1: #cycle
                return False
            if state[node] == 2: # visited
                return True
            state[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = 2
            return True
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False
        return True