class Solution {
    public int mostWordsFound(String[] sentences) {
        int m = 0; int a;char[] s;
        for(int i = 0; i < sentences.length; i++){
            a = 0;
            s = sentences[i].toCharArray();
            for(int j = 0; j < s.length; j++){
                if(s[j] == ' '){
                    a++;
                }
            }
            if(a>m){
                m = a;
            }
        }
        return m+1;
    }
}