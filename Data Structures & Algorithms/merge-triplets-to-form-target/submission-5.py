class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = second = third = False

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            first |= t[0] == target[0]
            second |= t[1] == target[1]
            third |= t[2] == target[2]

            if first and second and third:
                return True

        return False
