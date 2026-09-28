class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        boxes = [int(c) for c in boxes]
        left = boxes.copy()
        right = boxes.copy()

        for i in range(1, n):
            left[i] += left[i - 1]
            right[n - 1 - i] += right[n - i]

        for i in range(1, n):
            left[i] += left[i - 1]
            right[n - 1 - i] += right[n - i]

        left = [0] + left
        right = right + [0]

        return [left[i] + right[i + 1] for i in range(n)]
