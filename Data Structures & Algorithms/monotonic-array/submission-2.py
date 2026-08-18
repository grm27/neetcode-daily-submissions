class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        m_inc = m_dec = True

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                m_inc = False
            if nums[i] < nums[i + 1]:
                m_dec = False

        return m_inc or m_dec
