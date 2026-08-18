class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        m_inc = m_dec = True

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                m_inc = False
                break

        if m_inc:
            return True

        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                return False

        return True
