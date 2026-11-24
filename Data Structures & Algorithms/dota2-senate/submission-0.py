class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque([0 if c == "R" else 1 for c in senate])
        to_delete = [0, 0]

        while True:
            init_len = len(queue)

            for _ in range(init_len):
                next = queue.popleft()

                if to_delete[next] > 0:
                    to_delete[next] -= 1
                else:
                    queue.append(next)
                    to_delete[(next + 1) % 2] += 1

            if len(queue) == init_len:
                return "Radiant" if not queue[0] else "Dire"
