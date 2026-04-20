class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        fast = nums[fast] 

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

        i = 0
        while slow != i:
            i = nums[i]
            slow = nums[slow]
        
        return slow