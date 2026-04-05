class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            if len(count) == 3:
                new_count = defaultdict(int)
                for key in count:
                    count[key] -= 1
                    if count[key] > 0:
                        new_count[key] = count[key]
                count = new_count
        
        res = []
        for candidate in count:
            if nums.count(candidate) > len(nums) // 3:
                res.append(candidate)
        
        return res
                