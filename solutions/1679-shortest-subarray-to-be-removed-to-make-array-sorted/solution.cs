public class Solution {
    public int FindLengthOfShortestSubarray(int[] arr) {
        {
        int n = arr.Length;
        int left = 0, right = n - 1;

        // Find the longest non-decreasing prefix
        while (left < n - 1 && arr[left] <= arr[left + 1])
        {
            left++;
        }

        // If the entire array is already non-decreasing
        if (left == n - 1)
        {
            return 0;
        }

        // Find the longest non-decreasing suffix
        while (right > 0 && arr[right] >= arr[right - 1])
        {
            right--;
        }

        // Calculate the result by removing either prefix, suffix, or a middle subarray
        int result = Math.Min(n - left - 1, right); // Remove prefix or suffix

        // Try merging prefix and suffix
        int i = 0, j = right;
        while (i <= left && j < n)
        {
            if (arr[i] <= arr[j])
            {
                result = Math.Min(result, j - i - 1);
                i++;
            }
            else
            {
                j++;
            }
        }

        return result;
    }
}
    
}
