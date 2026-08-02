class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}

        def dfs(l, r, turn):
            state = (l, r, turn)
            if l == r:
                return piles[l] if turn else 0
            
            if state in cache:
                return cache[state]

            if turn:
                cache[state] = max(piles[l] + dfs(l + 1, r, not turn), piles[r] + dfs(l, r - 1, not turn))
            else:
                cache[state] = min(dfs(l + 1, r, not turn), dfs(l, r - 1, not turn))
            
            return cache[state]
        
        alice_score = dfs(0, len(piles) - 1, True)

        return alice_score > (sum(piles) - alice_score)