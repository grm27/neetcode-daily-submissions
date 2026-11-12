class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        num_set = set()
        total = 1 << k
        bit_mask = mask = total - 1

        num = 0
        for i in range(k):
            num <<= 1
            num |= ord(s[i]) - ord("0")

        num_set.add(num)
        for i in range(len(s) - k):
            num = num << 1 & bit_mask | (ord(s[i + k]) - ord("0"))
            num_set.add(num)
            if len(num_set) == total:
                return True

        return False
