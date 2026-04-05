class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        freq = len(nums) // 3
        
        res = []
        for el, c in count.items():
            if c > freq:
                res.append(el)
        
        return res