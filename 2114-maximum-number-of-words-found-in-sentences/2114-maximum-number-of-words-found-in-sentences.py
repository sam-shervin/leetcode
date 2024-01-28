class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m = 0
        for i in sentences:
            a = len(i.split(' '))
            if m<a:
                m = a
        return m
        