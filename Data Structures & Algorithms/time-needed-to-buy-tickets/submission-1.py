class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = 0
        queue = deque([(i, tkts) for i, tkts in enumerate(tickets)])

        while queue:
            t += 1
            i, tkts = queue.popleft()
            tkts -= 1
            if i == k and not tkts:
                return t

            if tkts:
                queue.append((i, tkts))
