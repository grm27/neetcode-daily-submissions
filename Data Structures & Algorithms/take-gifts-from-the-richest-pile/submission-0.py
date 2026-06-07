class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            max_pile = heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(-max_pile)))
        
        return -sum(gifts)