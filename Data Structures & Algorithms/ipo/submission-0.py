class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        final_capital = w
        capital = [(c, i) for i, c in enumerate(capital)]
        heapq.heapify(capital)
        max_p_heap = []

        for _ in range(k):
            while capital and final_capital >= capital[0][0]:
                c, i = heapq.heappop(capital)
                heapq.heappush(max_p_heap, -profits[i])
            if not max_p_heap:
                break
            final_capital += -heapq.heappop(max_p_heap)

        return final_capital
