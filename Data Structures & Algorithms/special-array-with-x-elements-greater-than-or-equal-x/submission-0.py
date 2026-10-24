class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 1, n

        while l < r:
            m = (l + r) // 2

            if sum(nums[i] >= m for i in range(n)) > m:
                l = m + 1
            else:
                r = m

        return l if l == sum(nums[i] >= l for i in range(n)) else -1
