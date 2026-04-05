class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        existing = set()

        for i in range(min(k + 1, len(nums))):
            if nums[i] not in existing:
                existing.add(nums[i])
            else:
                return True
        
        for i in range(k + 1, len(nums)):
            existing.remove(nums[i - k - 1])
            if nums[i] in existing:
                return True
            else:
                existing.add(nums[i])
        
        return False