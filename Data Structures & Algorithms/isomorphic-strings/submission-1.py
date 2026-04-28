class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        mapping_dict = {}
        reverse_mapping_dict = {}

        for i in range(n):
            if s[i] in mapping_dict and t[i] != mapping_dict[s[i]] or t[i] in reverse_mapping_dict and reverse_mapping_dict[t[i]] != s[i]:
                return False
            mapping_dict[s[i]] = t[i]
            reverse_mapping_dict[t[i]] = s[i]
        
        return True