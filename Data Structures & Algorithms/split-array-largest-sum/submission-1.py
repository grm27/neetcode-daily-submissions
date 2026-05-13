class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(largest):
            subarrays = 1
            curr_sum = 0
            for n in nums:
                curr_sum += n
                if curr_sum > largest:
                    subarrays += 1
                    curr_sum = n
                if subarrays > k:
                    return False
            
            return True
        
        left, right = max(nums), sum(nums)
        res = right
        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
                res = min(res, mid)
            else:
                left = mid + 1
        
        return res