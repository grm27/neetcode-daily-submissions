class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = defaultdict(lambda: -1)
        stack = []

        for i, n in enumerate(nums2):
            while stack and n > stack[-1]:
                greater[stack[-1]] = n
                stack.pop()

            stack.append(n)

        return [greater[n] for n in nums1]
