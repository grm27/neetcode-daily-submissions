class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)

        diff = 0
        for i, height in enumerate(heights):
            if height != expected[i]:
                diff += 1
        
        return diff