class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        digit_count = defaultdict(int)

        for i in range(3):
            digit_count[ord(num[i]) - ord("0")] += 1
        
        max_digit = -1
        res = ""
        for i in range(n - 3 + 1):
            digit = ord(num[i]) - ord("0")
            if digit_count[digit] == 3 and digit > max_digit:
                res = num[i: i + 3]
                max_digit = digit
            
            if i < n - 3:
                digit_count[digit] -= 1
                if digit_count[digit] == 0:
                    del digit_count[digit]
                next_digit = ord(num[i + 3]) - ord("0")
                digit_count[next_digit] += 1
        
        return res

