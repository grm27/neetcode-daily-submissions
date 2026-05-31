class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        cache = {}

        def dfs(i, curr_amount):
            state = (i, curr_amount)
            
            if state in cache:
                return cache[state]

            if curr_amount > amount:
                return 0
            
            if curr_amount == amount:
                return 1
            
            res = 0
            for j in range(i, n):
                res += dfs(j, curr_amount + coins[j])
            cache[state] = res
            return res
        
        return dfs(0, 0)