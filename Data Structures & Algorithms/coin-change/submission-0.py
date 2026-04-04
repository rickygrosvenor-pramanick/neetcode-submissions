class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        B = [10001] * (amount + 1)
        B[0] = 0
        C = [-1] * (amount + 1)

        for i in range(1, amount + 1):
            minimum = B[i]
            denom_for_min_coin = -1
            for j in coins:
                if i >= j:
                    if 1 + B[i - j] < minimum:
                        minimum = 1 + B[i - j]
                        denom_for_min_coin = j
            
            C[i] = denom_for_min_coin
            B[i] = minimum
        
        if B[amount] == 10001:
            return -1
        
        curr = amount
        ret = []
        while curr != 0:
            ret.append(C[curr])
            curr = curr - C[curr]
        
        return len(ret)