class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        serverQueue = []
        processingQueue = []
        res = [0] * len(tasks)

        for i in range(len(servers)):
            heapq.heappush(serverQueue, (servers[i], i))

        t = 0
        for i in range(len(tasks)):
            t = max(t, i)

            if len(serverQueue) == 0:
                t = processingQueue[0][0]

            # add the available servers at time t to server queue
            while processingQueue and processingQueue[0][0] <= t:
                endTime, serverI = heapq.heappop(processingQueue)
                heapq.heappush(serverQueue, (servers[serverI], serverI))

            nextServerIndex = heapq.heappop(serverQueue)[1]
            res[i] = nextServerIndex
            heapq.heappush(processingQueue, (t + tasks[i], nextServerIndex))

        return res
