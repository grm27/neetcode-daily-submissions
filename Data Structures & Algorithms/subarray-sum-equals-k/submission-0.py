class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_dict = {}
        prefix_dict[0] = 1
        prefix_sum = 0
        res = 0

        for i in range(n):
            prefix_sum += nums[i]
            if prefix_sum - k in prefix_dict:
                res += prefix_dict[prefix_sum - k]
            
            prefix_dict[prefix_sum] = (
                prefix_dict[prefix_sum] + 1 if prefix_sum in prefix_dict else 1
            )
        
        return res


