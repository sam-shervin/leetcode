class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s;
        newString = ""
        interval = 2*numRows-2;
        for i in range(0, numRows):
            if i==0:
                for j in range(0,len(s), interval):
                    newString+=s[j];
            elif i==numRows-1:
                for j in range(numRows-1,len(s), interval):
                    newString+=s[j];
            else:
                for j in range(i,len(s), (interval)):
                    newString+=s[j];
                    try:
                        print(j, j+interval-2*i)
                        newString+=s[j+interval-2*i]
                    except IndexError:
                        pass
                
        return newString;
        
        
"""5:
8
6 2
4 4
2 6
8

4:
6
4 2
2 4
6
    
3:
4
2 2
4

2:
2
2
    
1:
1"""