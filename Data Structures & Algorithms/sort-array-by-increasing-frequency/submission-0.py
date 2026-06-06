class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count_dict = Counter(nums)
        nums.sort(key=lambda x: (count_dict[x], -x))
        return nums
