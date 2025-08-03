class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        le = len(s)
        cuts = {0}

        for i in range(1, le + 1):
            for j in list(cuts):
                if s[j:i] in wordDict:
                    cuts.add(i)
                    break

        return le in cuts
