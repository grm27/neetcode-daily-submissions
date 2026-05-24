class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for p in points:
            x, y = p
            heapq.heappush(min_heap, (-(x*x + y*y), p))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [p for _, p in min_heap]