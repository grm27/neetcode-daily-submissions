class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []

        for n in nums:
            left, right = 0, len(lis)

            while left < right:
                mid = (left + right) // 2

                if lis[mid] < n:
                    left = mid + 1
                else:
                    right = mid

            if left == len(lis):
                lis.append(n)
            else:
                lis[left] = n

        return len(lis)
