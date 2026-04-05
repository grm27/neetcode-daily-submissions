class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            if len(count) == 3:
                to_del = []
                for key in count:
                    count[key] -= 1
                    if count[key] == 0:
                        to_del.append(key)
                for key in to_del:
                    del count[key]
        
        res = []
        for candidate in count:
            c = 0
            for n in nums:
                if n == candidate:
                    c += 1
            if c > len(nums) // 3:
                res.append(candidate)
        
        return res
                