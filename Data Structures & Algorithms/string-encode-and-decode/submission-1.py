class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStrings = []
        for s in strs:
            if not s:
                encodedStrings.append("#")
            else:
                encodedStrings.append(",".join(str(ord(c)) for c in s))
        return " ".join(encodedStrings)

    def decode(self, s: str) -> List[str]:
        res = []

        if not s:
            return res

        for string in s.split(" "):
            if string == "#":
                res.append("")
            else:
                res.append("".join(chr(int(c)) for c in string.split(",")))
        return res