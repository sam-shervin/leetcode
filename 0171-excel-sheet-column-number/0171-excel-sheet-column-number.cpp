
class Solution {
public:
    int titleToNumber(string columnTitle) {
        int a = 0;
        for(int i=columnTitle.size()-1; i>=0; i--){
            a += pow(26,(columnTitle.size()-1-i))*(columnTitle[i]-64);
        }
        return a;    
    }
};

