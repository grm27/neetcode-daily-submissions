class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dec_queue, inc_queue = deque(), deque()
        l = res = 0

        for r in range(len(nums)):
            n = nums[r]

            while dec_queue and n > dec_queue[-1]:
                dec_queue.pop()
            while inc_queue and n < inc_queue[-1]:
                inc_queue.pop()

            dec_queue.append(n)
            inc_queue.append(n)

            while dec_queue[0] - inc_queue[0] > limit:
                if nums[l] == dec_queue[0]:
                    dec_queue.popleft()
                if nums[l] == inc_queue[0]:
                    inc_queue.popleft()
                l += 1

            res = max(r - l + 1, res)

        return res
