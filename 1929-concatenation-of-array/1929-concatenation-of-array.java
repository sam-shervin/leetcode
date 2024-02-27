class Solution {
    public int[] getConcatenation(int[] nums) {
        int len = nums.length;
        int[] num = new int[2*len];
        for(int i=0; i<len; i++){
            num[i] = num[i+len] = nums[i];
        }
        return num;
    }
}