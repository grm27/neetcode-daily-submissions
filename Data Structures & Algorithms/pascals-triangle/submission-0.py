class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            curr_row = [1] * (i + 1)
            prev_row = res[i - 1]

            for j in range(1, i):
                curr_row[j] = prev_row[j - 1] + prev_row[j]

            res.append(curr_row)

        return res
