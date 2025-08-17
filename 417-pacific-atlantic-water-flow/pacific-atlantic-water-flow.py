class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        atlantic = [[False]*n for _ in range(m)]
        pacific = [[False]*n for _ in range(m)]
        rel = [[-1,0], [0, 1], [1, 0], [0, -1]]
        def dfs(r, c, visited):
            visited[r][c] = True
            for xrel, yrel in rel:
                cx = xrel+c
                cy = yrel+r
                if 0<=cy<m and 0<=cx<n:
                    if not visited[cy][cx] and heights[r][c]<=heights[cy][cx]:
                        dfs(cy, cx, visited)
        for c in range(n):
            dfs(0, c, pacific)
        for r in range(m):
            dfs(r, 0, pacific)

        for c in range(n):
            dfs(m-1, c, atlantic)
        for r in range(m):
            dfs(r, n-1, atlantic)
        
        res = []
        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])
        
        return res


