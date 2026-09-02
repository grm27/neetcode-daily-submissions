class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            j, min_len = 0, min(len(w1), len(w2))

            while j < min_len and order_dict[w1[j]] == order_dict[w2[j]]:
                j += 1

            if (
                j == min_len
                and len(w1) > len(w2)
                or j < min_len
                and order_dict[w1[j]] > order_dict[w2[j]]
            ):
                return False

        return True
