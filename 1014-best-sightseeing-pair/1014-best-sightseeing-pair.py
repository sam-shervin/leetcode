class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        a = values[0]
        maxi = a
        for i in range(1, len(values)):
            maxi = max(maxi, a + values[i]-i)
            a = max(a, values[i]+i)
        return maxi
        