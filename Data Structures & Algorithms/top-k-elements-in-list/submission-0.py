class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        min_heap = []

        for el, c in count.items():
            heapq.heappush(min_heap, (c, el))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [el for c, el in min_heap]