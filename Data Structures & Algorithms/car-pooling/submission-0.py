class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_heap = []

        for p, f, t in trips:
            heapq.heappush(min_heap, (f, p))
            heapq.heappush(min_heap, (t, -p))
        
        max_pass = 0
        total_passengers = 0
        while min_heap:
            total_passengers += heapq.heappop(min_heap)[1]
            if total_passengers > capacity:
                return False
        
        return True