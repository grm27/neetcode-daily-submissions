class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = nums.copy()
        suffix_product = nums.copy()

        for i in range(1, n):
            prefix_product[i] *= prefix_product[i - 1]
        for i in range(n - 2, -1, -1):
            suffix_product[i] *= suffix_product[i + 1]

        res = [0] * n
        for i in range(1, n - 1):
            res[i] = prefix_product[i - 1] * suffix_product[i + 1]

        res[0] = suffix_product[1]
        res[-1] = prefix_product[-2]

        return res
