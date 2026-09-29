class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        a, b = len(str1), len(str2)
        while a % b != 0:
            r = a % b
            a = b
            b = r

        gcd = str1[:b]

        for i in range(len(str1) // b):
            if str1[i * b : (i + 1) * b] != gcd:
                return ""

        for i in range(len(str2) // b):
            if str2[i * b : (i + 1) * b] != gcd:
                return ""

        return gcd
