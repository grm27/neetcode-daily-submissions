class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[k], nums[j] = nums[j], nums[k]
                k += 1
        
        return k