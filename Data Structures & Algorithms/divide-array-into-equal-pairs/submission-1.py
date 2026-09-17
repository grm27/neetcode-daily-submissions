class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        for c in Counter(nums).values():
            if c % 2:
                return False

        return True
