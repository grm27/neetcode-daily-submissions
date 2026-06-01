class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = Counter(s)
        max_heap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(max_heap)

        if -max_heap[0][0] > len(s) // 2 + len(s) % 2:
            return ""

        res = []
        prev_char, prev_count = "", 0
        while max_heap:
            count, char = heapq.heappop(max_heap)
            res.append(char)

            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))

            prev_char, prev_count = char, count + 1

        return "".join(res)


