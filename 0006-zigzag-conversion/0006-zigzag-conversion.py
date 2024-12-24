class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s;
        newString = ""
        if numRows == 2:
            for i in range(0, len(s), 2):
                newString+=s[i]
            for i in range(1,len(s),2):
                newString+=s[i]
            return newString
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
                    if j + interval - 2*i < len(s):
                        newString += s[j + interval - 2*i]
        return newString;
        