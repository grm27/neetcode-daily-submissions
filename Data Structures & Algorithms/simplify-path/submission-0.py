class Solution:
    def simplifyPath(self, path: str) -> str:
        elements = path.split("/")
        res = []

        for el in elements:
            if not el or el == ".":
                continue

            if el == "..":
                if res:
                    res.pop()
            else:
                res.append(el)

        return "/" + "/".join(res)
