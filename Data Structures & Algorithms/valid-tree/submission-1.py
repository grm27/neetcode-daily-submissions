class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        def has_no_cycle(prev, curr_node):
            if visited[curr_node]:
                return False
            
            visited[curr_node] = True
            for nei in graph[curr_node]:
                if nei != prev and not has_no_cycle(curr_node, nei):
                    return False
            return True
        
        return has_no_cycle(-1, 0) and visited.count(True) == n