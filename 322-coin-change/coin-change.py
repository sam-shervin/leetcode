from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort(reverse=True)  # larger coins first (better pruning)
        visited = set([0])
        queue = deque([(0, 0)])  # (current_amount, steps)

        while queue:
            curr, steps = queue.popleft()
            for c in coins:
                nxt = curr + c
                if nxt == amount:
                    return steps + 1
                if nxt < amount and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
        return -1
