class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            a, b = edges[i]
            p = succProb[i]
            graph[a].append((b, p))
            graph[b].append((a, p))
        
        largest_prob = [0] * n
        largest_prob[start_node] = 1
        max_heap = [(-1, start_node)]

        while max_heap:
            prob, node = heapq.heappop(max_heap)

            if -prob < largest_prob[node]:
                continue
            
            if node == end_node:
                return -prob
            
            for nei, p in graph[node]:
                new_prob = -prob * p
                if new_prob > largest_prob[nei]:
                    heapq.heappush(max_heap, (-new_prob, nei))
                    largest_prob[nei] = new_prob

        return 0