class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        // Map rule keys to their corresponding indices
        unordered_map<string, int> ruleIndices = {{"type", 0}, {"color", 1}, {"name", 2}};
        
        // Check if the ruleKey exists in the map
        if (ruleIndices.find(ruleKey) == ruleIndices.end()) {
            return 0; // If not found, return 0
        }
        
        int index = ruleIndices[ruleKey];
        int count = 0;
        
        // Iterate through items and count matches
        for (const auto& item : items) {
            if (item[index] == ruleValue) {
                count++;
            }
        }
        
        return count;
    }
};