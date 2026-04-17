class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        res = []
        i = 0
        while i < n - 2:
            left = i + 1
            right = n  - 1
            target = -nums[i]
          
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                else:
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1             

            while i < n - 2 and nums[i] == nums[i + 1]:
                i +=1
            i += 1
        
        return res
            
                