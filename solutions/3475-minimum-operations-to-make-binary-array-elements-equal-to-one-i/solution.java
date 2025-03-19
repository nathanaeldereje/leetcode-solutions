class Solution {
    public int minOperations(int[] nums) {
        if (nums.length < 3) return -1;  // Ensure we have at least 3 elements

        int operations = 0;

        // Iterate through the array to flip segments of 3
        for (int i = 0; i <= nums.length - 3; i++) {
            if (nums[i] == 0) {  // Found a 0, flip a segment of 3 elements
                for (int j = 0; j < 3; j++) {
                    nums[i + j] = nums[i + j] == 0 ? 1 : 0;
                }
                operations++;  // Increment the number of operations
            }
        }

        // Check if there are any 0s remaining in the array
        for (int num : nums) {
            if (num == 0) {
                return -1;  // If a 0 is found, return -1
            }
        }

        return operations;  
    }
}
