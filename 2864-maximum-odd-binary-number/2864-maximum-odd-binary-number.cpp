class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int count_1=0, count_0;
        for(int i=0; i<s.length(); i++){
            if (s.at(i) == '1'){
                count_1++;
            }
        }
        count_0 = s.length()-count_1; s.erase();
        for(int i=0; i<count_1-1; i++){
            s+="1";
        }
        for(int i=0; i<count_0; i++){
            s+="0";
        }
        s+="1";
        return s;
    }
};