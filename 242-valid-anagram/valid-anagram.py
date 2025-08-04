class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)
        for i in s:
            dic[i]+=1
        for i in t:
            dic[i]-=1
        return True if all(x == 0 for x in dic.values()) else False