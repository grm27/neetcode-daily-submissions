class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []

        for char, count in [("a", a), ("b", b), ("c", c)]:
            if count:
                heapq.heappush(max_heap, (-count, char))

        res = []
        stale = None
        while max_heap:
            next_char = heapq.heappop(max_heap)

            if len(res) > 1 and res[-2] == res[-1] == next_char[1]:
                stale = next_char
            else:
                res.append(next_char[1])
                if next_char[0] < -1:
                    heapq.heappush(max_heap, (next_char[0] + 1, next_char[1]))
                if stale:
                    heapq.heappush(max_heap, stale)
                    stale = None

        return "".join(res)
