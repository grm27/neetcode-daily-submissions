class Solution:
    def addBinary(self, a: str, b: str) -> str:
        digits_a = [ord(c) - ord("0") for c in a[::-1]]
        digits_b = [ord(c) - ord("0") for c in b[::-1]]
        res = []
        carry_over = 0

        if len(a) < len(b):
            digits_a, digits_b = digits_b, digits_a

        for i in range(min(len(a), len(b))):
            res.append(str(carry_over ^ digits_a[i] ^ digits_b[i]))
            carry_over = digits_a[i] + digits_b[i] + carry_over > 1

        for i in range(min(len(a), len(b)), max(len(a), len(b))):
            res.append(str(carry_over ^ digits_a[i]))
            carry_over &= digits_a[i]

        if carry_over:
            res.append("1")

        return "".join(res[::-1])
