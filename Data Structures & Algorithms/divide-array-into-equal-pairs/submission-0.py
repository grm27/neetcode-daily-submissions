class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for _, c in count.items():
            if c % 2 == 1:
                return False

        return True
