class Solution {
public:
    string interpret(string command) {
        int i=0;
        string output = "";
        while(true){
            char a = command.at(i);
            if (a != '('){
                output = output + 'G';
                i++;
            }else{
                i++;
                if (command.at(i) == ')'){
                    output = output + 'o';
                    i++;
                } else {
                    output = output + "al";
                    i=i+3;
                }
            }
            if (i>command.size()-1){
                break;
            }
        }
        return output;
    }
};