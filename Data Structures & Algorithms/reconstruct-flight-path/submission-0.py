class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for from_i, to_i in tickets:
            heapq.heappush(graph[from_i], to_i)
        
        res = []
        def dfs(node):
            while graph[node]:
                next_node = heapq.heappop(graph[node])
                dfs(next_node)
            res.append(node)

        dfs("JFK")
        return res[::-1]