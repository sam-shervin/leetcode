class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        a = []
        a.append(first)
        for i in range(len(encoded)):
            a.append(a[i] ^ encoded[i])
        return a
            