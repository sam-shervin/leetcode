class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        a = [[1], [1, 1]]
        
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(a[i-1][j-1] + a[i-1][j])
            row.append(1)
            a.append(row)
        
        return a

