class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        def can_ship_within_days(capacity):
            d = 1
            load = 0

            for w in weights:
                load += w
                if load > capacity:
                    load = w
                    d += 1
                if d > days:
                    return False
                
            return True
        
        while left < right:
            mid = (left + right) // 2
            
            if can_ship_within_days(mid):
                right = mid
            else:
                left = mid + 1
        
        return left