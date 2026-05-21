class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        def find_peak():
            left, right = 0, mountainArr.length() - 1

            while left < right:
                mid = (left + right) // 2

                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid

            return left

        def bin_search(left, right):
            while left < right:
                mid = (left + right) // 2

                if mountainArr.get(mid) < target:
                    left = mid + 1
                else:
                    right = mid

            return left
        
        def rev_bin_search(left, right):
            while left < right:
                mid = (left + right) // 2

                if mountainArr.get(mid) <= target:
                    right = mid
                else:
                    left = mid + 1

            return left
        
        peak = find_peak()

        first_half_res = bin_search(0, peak)
        if mountainArr.get(first_half_res) == target:
            return first_half_res
        
        second_half_res = rev_bin_search(peak + 1, mountainArr.length() - 1)
        
        return -1 if mountainArr.get(second_half_res) != target else second_half_res