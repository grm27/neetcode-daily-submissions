class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        total = answer = 0
        for i, x in enumerate(nums):
            total += x
            counts[x] += 1
            if i >= k:
                old = nums[i - k]
                total -= old
                counts[old] -= 1
                if counts[old] == 0:
                    del counts[old]
            if i >= k - 1 and len(counts) == k:
                answer = max(answer, total)
        return answer
