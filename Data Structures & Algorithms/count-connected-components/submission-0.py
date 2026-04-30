class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        visited = [False] * n
        def dfs(node):
            if visited[node]:
                return

            visited[node] = True
            for nei in graph[node]:
                dfs(nei)
        
        res = 0 
        for i in range(n):
            if not visited[i]:
                res += 1
                dfs(i)
        
        return res
            