class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = [-freq for _, freq in Counter(tasks).items()]
        heapq.heapify(max_heap)
        waiting_queue = deque()

        t = 0
        while max_heap or waiting_queue:
            while waiting_queue and t > waiting_queue[0][0]:
                heapq.heappush(max_heap, -waiting_queue.popleft()[1])

            if max_heap:
                freq = -heapq.heappop(max_heap)
                freq -= 1
                if freq:
                    waiting_queue.append((t + n, freq))
            t += 1

        return t
