class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        queue = deque()
        res = []

        for i in range(k):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])

        res.append(queue[0])

        for i in range(n - k):
            while queue and queue[-1] < nums[i + k]:
                queue.pop()

            queue.append(nums[i + k])

            if queue[0] == nums[i]:
                queue.popleft()

            res.append(queue[0])

        return res
