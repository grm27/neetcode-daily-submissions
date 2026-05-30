class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        n = len(customers)
        unsatisfied = [customers[i] * grumpy[i] for i in range(n)]

        unsatisfied_sum = sum(unsatisfied[i] for i in range(minutes))

        start = 0
        max_s = 0
        for i in range(n - minutes + 1):
            if unsatisfied_sum > max_s:
                max_s = unsatisfied_sum
                start = i

            if i < n - minutes:
                max_s = max_s - unsatisfied[i + minutes] + unsatisfied[i]

        for i in range(start, start + minutes):
            grumpy[i] = 0

        return sum(customers[i] * (1 - grumpy[i]) for i in range(n))
