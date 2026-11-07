class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_server_queue = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free_server_queue)
        busy_server_queue = []
        task_queue = deque()
        t = 0
        res = [0] * len(tasks)

        while task_queue or t < len(tasks):
            # enqueue ready tasks
            if t < len(tasks):
                task_queue.append((tasks[t], t))

            # free servers
            while busy_server_queue and busy_server_queue[0][0] <= t:
                _, weight, index = heapq.heappop(busy_server_queue)
                heapq.heappush(free_server_queue, (weight, index))

            # enqueue task execution
            while task_queue and free_server_queue:
                weight, s_index = heapq.heappop(free_server_queue)
                time, t_index = task_queue.popleft()
                heapq.heappush(busy_server_queue, (t + time, weight, s_index))
                res[t_index] = s_index

            if t < len(tasks):
                t += 1
            else:
                t = busy_server_queue[0][0]

        return res
