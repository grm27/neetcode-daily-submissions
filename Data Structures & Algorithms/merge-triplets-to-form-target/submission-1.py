class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = second = third = False

        for t in triplets:
            first |= t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2]
            second |= t[1] == target[1] and t[0] <= target[0] and t[2] <= target[2]
            third |= t[2] == target[2] and t[0] <= target[0] and t[1] <= target[1]

        return first & second & third
