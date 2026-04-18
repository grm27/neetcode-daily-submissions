class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed = 0
        n = x
        while n > 0:
            reversed = reversed * 10 + n % 10
            n //= 10
        
        return reversed == x