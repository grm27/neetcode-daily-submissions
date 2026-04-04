class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            groups[self._hash(s)].append(s)
        
        return list(groups.values())
    
    def _hash(self, s):
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        return str(count)