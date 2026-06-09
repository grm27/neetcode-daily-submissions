class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            curr_sum = 0

            while n > 0:
                digit = n % 10
                curr_sum += digit * digit
                n //= 10
            
            if curr_sum == 1:
                return True
            
            n = curr_sum
        
        return False
