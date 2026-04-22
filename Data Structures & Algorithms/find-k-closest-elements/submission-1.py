class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = 0, n - 1

        while right - left >= k:
            if abs(arr[right] - x) >= abs(arr[left] - x):
                right -= 1
            else:
                left += 1

        return arr[left : right + 1]
