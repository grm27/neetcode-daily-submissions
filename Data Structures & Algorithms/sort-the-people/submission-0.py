class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        aggregate = list(zip(heights, names))
        aggregate.sort(key=lambda x: -x[0])
        return [name for h, name in aggregate]
