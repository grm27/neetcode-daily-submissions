class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        queue = deque()
        res = []

        for i in range(k):
            while queue and queue[-1][0] < nums[i]:
                queue.pop()
            queue.append((nums[i], i))

        for i in range(n - k + 1):
            res.append(queue[0][0])

            if i == n - k:
                break

            while queue and queue[-1][0] < nums[i + k]:
                queue.pop()

            queue.append((nums[i + k], i + k))

            if queue[0][1] == i:
                queue.popleft()

        return res
