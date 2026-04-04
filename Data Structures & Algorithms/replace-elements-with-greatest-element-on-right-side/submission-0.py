class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_el = arr[-1]
        prev = -1
        arr[-1] = -1
    
        for i in range(len(arr) - 2, -1, -1):
            prev = arr[i]
            arr[i] = max_el
            max_el = max(max_el, prev)
        
        return arr