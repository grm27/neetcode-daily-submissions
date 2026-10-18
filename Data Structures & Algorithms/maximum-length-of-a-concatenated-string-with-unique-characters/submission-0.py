class Solution:
    def maxLength(self, arr: List[str]) -> int:
        bit_masks = []

        for s in arr:
            bit_mask = 0
            invalid = False
            for c in s:
                char_index = ord(c) - ord("a")
                if 1 << char_index & bit_mask > 0:
                    invalid = True
                    break
                bit_mask |= 1 << char_index
            if not invalid:
                bit_masks.append(bit_mask)

        cache = {}

        def backtrack(i, curr_seq):
            if i == len(bit_masks):
                return curr_seq.bit_count()

            if (i, curr_seq) in cache:
                return cache[(i, curr_seq)]

            res = 0
            for j in range(i, len(bit_masks)):
                if curr_seq & bit_masks[j] == 0:
                    res = max(res, backtrack(j + 1, curr_seq | bit_masks[j]))
                else:
                    res = max(res, backtrack(j + 1, curr_seq))

            cache[(i, curr_seq)] = res
            return res

        return backtrack(0, 0)
