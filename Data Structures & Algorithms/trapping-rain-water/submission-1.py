class Solution:
    def trap(self, height: List[int]) -> int:
        baseline = 0
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            h = min(height[l], height[r])
            res += (r - l + 1) * max(0, h - baseline)
            baseline = max(baseline, h)

            if height[l] < height[r]:
                res -= height[l]
                l += 1
            else:
                res -= height[r]
                r -= 1

        return res - baseline
