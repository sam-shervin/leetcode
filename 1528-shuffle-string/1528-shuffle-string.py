class Solution:
    def myfunc(self, a):
        return a[1]
    def restoreString(self, s: str, indices: List[int]) -> str:
        lis = [(s[i], indices[i]) for i in range(len(s))]
        lis.sort(key=self.myfunc)
        s = ""
        for i in lis:
            s+= i[0]
        return s
            