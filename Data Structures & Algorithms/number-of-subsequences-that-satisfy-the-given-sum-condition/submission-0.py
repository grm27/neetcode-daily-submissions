class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        nums.sort()

        res = 0
        right = n - 1
        for i in range(n):
            if nums[i] * 2 > target:
                break

            while nums[i] + nums[right] > target and right > i:
                right -= 1

            res += 2 ** (right - i)
            res %= mod

        return res
