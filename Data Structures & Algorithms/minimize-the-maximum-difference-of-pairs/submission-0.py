class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()

        if p == 0:
            return 0

        def can_find_p_pairs(diff):
            i = 0
            pairs = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= diff:
                    pairs += 1
                    i += 2
                else:
                    i += 1
                if pairs == p:
                    return True

            return False

        l, r = 0, 10**9

        while l < r:
            m = (l + r) // 2

            if can_find_p_pairs(m):
                r = m
            else:
                l = m + 1

        return l
