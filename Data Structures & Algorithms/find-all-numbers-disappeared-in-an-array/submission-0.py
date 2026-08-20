class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        present = [False] * n

        for num in nums:
            present[num - 1] = True

        return [num + 1 for num in range(n) if not present[num]]
