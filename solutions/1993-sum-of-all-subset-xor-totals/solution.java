class Solution {
    public int subsetXORSum(int[] nums) {
        
        int xor=0;
        for(int i=0;i<nums.length;i++){
            xor=xor|nums[i];
        }
    //    for(int i=0;i<nums.length;i++){
    //         xor+=nums[i];
    //    }

    
        return xor<<(nums.length-1);
    }
}
