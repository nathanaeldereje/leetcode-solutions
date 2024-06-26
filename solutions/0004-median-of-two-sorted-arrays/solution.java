class Solution {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        int sizeN = m + n;
        int[] arr = new int[m + n];
        System.arraycopy(nums1, 0, arr, 0, m);
        System.arraycopy(nums2, 0, arr, m, n);
        Arrays.sort(arr);
        if (sizeN % 2 == 0) {
            return (arr[sizeN / 2] + arr[sizeN / 2 -1]) / 2.0;
        } else {
            return arr[sizeN / 2];
        }

    }  
         
}
