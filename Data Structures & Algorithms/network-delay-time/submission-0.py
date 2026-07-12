class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        
        for u, v, time in times:
            graph[u - 1].append((v - 1, time))

        cost = [float("inf")] * n
        min_heap = [(0, k - 1)]
        cost[k - 1] = 0

        while min_heap:
            node_time, node = heapq.heappop(min_heap)

            for nei, t in graph[node]:
                new_nei_cost = node_time + t
                if new_nei_cost < cost[nei]:
                    cost[nei] = new_nei_cost
                    heapq.heappush(min_heap, (new_nei_cost, nei))
        
        res = max(cost)
        return res if res < float("inf") else -1