class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        parent = [-1] * n
        depth = [0] * n
        order = [0]
        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)
        bobtime = [n] * n
        u = bob
        t = 0
        while u != -1:
            bobtime[u] = t
            t += 1
            u = parent[u]
        profit = [0] * n
        answer = -1000000000
        for u in order:
            gain = (
                amount[u]
                if depth[u] < bobtime[u]
                else amount[u] // 2
                if depth[u] == bobtime[u]
                else 0
            )
            profit[u] = gain + (profit[parent[u]] if u != 0 else 0)
            if u != 0 and len(graph[u]) == 1:
                answer = max(answer, profit[u])
        return answer
