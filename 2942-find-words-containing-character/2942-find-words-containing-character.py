class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        lis = []
        for i in range(len(words)):
            if x in words[i]:
                lis.append(i)
        return lis