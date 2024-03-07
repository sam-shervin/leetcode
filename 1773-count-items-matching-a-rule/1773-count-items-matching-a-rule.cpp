class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int index, count=0;
        if (ruleKey == "type"){
            index = 0;
        }else if (ruleKey == "color"){
            index = 1;
        }else if (ruleKey == "name"){
            index = 2;
        }
        for(int i=0; i<items.size(); i++){
            if (ruleValue == items[i][index]){
                count++;
            }
        }
        return count;
    }
};