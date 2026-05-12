class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        value_count = defaultdict(int)
        res = 0

        for n in nums:
            res += value_count[n]
            value_count[n] += 1
        
        return res