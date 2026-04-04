class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
            
        dp1 = [0] * (n + 1)
        dp2 = [0] * (n + 1)

        nums1 = nums[:n]
        nums2 = nums[1:]

        for i in range(n - 1):
            dp1[i + 2] = max(dp1[i + 1], nums1[i] + dp1[i])
            dp2[i + 2] = max(dp2[i + 1], nums2[i] + dp2[i])
        
        return max(dp1[n], dp2[n])