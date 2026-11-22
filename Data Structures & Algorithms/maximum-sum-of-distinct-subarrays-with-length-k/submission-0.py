class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = sub_sum = dist_values = 0
        count = defaultdict(int)

        for i in range(k):
            sub_sum += nums[i]
            count[nums[i]] += 1
            dist_values += (count[nums[i]] == 1) - (count[nums[i]] == 2)

        for i in range(n - k + 1):
            if dist_values == k:
                res = max(res, sub_sum)

            if i < n - k:
                count[nums[i]] -= 1
                dist_values += (count[nums[i]] == 1) - (count[nums[i]] == 0)

                count[nums[i + k]] += 1
                dist_values += (count[nums[i + k]] == 1) - (count[nums[i + k]] == 2)

                sub_sum += -nums[i] + nums[i + k]

        return res
