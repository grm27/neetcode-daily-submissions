class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        
        count = [0] * 26
        for c in s1:
            count[ord(c) - ord("a")] += 1
        
        window_matching_chars = 0
        for i in range(m):
            char_index = ord(s2[i]) - ord("a")
            if count[char_index] > 0:
                window_matching_chars += 1
            count[char_index] -= 1

        for i in range(n - m + 1):
            if window_matching_chars == m:
                return True
            if i < n - m:
                to_remove_index = ord(s2[i]) - ord("a")
                to_add_index = ord(s2[i + m]) - ord("a")
                
                count[to_remove_index] += 1
                if count[to_remove_index] > 0:
                    window_matching_chars -= 1
               
                if count[to_add_index] > 0:
                    window_matching_chars += 1
                count[to_add_index] -= 1
      
        
        return False

            
            

