class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % k:
            return False

        nums.sort(reverse=True)
        target = total // k
        used = [False] * n

        def backtrack(i, k, subset_sum):
            if k == 0:
                return True

            if target == subset_sum:
                return backtrack(0, k - 1, 0)

            for j in range(i, n):
                if used[j] or subset_sum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subset_sum + nums[j]):
                    return True
                used[j] = False

            return False

        return backtrack(0, k, 0)
