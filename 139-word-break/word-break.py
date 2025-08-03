class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        le = len(s)
        dp = [False] * (le + 1)
        dp[0] = True

        for i in range(1, le + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break 

        return dp[le]
