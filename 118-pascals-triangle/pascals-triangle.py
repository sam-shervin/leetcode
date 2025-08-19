class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        if numRows == 1:
            return [[1]]
        else:
            a = [[1],[1,1]]
            i = len(a)
            while not i==numRows:
                a.append([])
                a[i].append(1)
                for x in range(1, i):
                    a[i].append(a[i-1][x-1]+a[i-1][x])
                a[i].append(1)
                i+=1
            return a

