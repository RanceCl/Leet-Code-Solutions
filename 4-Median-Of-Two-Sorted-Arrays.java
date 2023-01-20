/*
Two sorted arrays, nums1 of size n, and nums2 of size m, 
were provided, intent of returning the over all median of
the two sorted arrays. 

The overall run time complexity was required to be 
O(log(m+n)).

Binary search was used to find the median.
To find the median of an array, only the left half of
the array is necessary. 

To determine which elements in each array actually
contribute (are in the left half of the merged array),
the two input arrays can be split into two subarrays:
    nums1L with elements nums1 [ 0 to i ],
    nums1R with elements nums1 [ i+1 to n-1 ],
    nums2L with elements nums2 [ 0 to j ],
    nums2R with elements nums2 [ j+1 to m-1 ], 

The correct partition for the contributing elements will 
be such that: 
    nums1[i-1] <= nums2[j]
    nums2[j-1] <= nums1[i]
*/
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int l1, l2, r1, r2;
        int lo, hi;
        int mid1, mid2;
        int n = nums1.length;
        int m = nums2.length;
        int merge_med;

       // First array must be smaller
        if(n > m)
            return findMedianSortedArrays(nums2, nums1);

        // Index of the median in the merged array
        merge_med = (n+m+1)/2;
        lo=0;
        hi=n; 

        // Edge cases
        // If array one is empty, only find the median of array two
        if(n==0)
        {
            // Average of two medians if even length
            if(m%2 == 0)
                return (nums2[m/2]+nums2[m/2-1])/2.0;
            // Only one median if odd length
            else
                return nums2[m/2];
        }

        // If array two is empty, only find the median of array one
        if(m==0)
        {
            // Average of two medians if even length
            if(n%2 == 0)
                return (nums1[n/2]+nums1[n/2-1])/2.0;
            // Only one median if odd length
            else
                return nums1[n/2];

        }
        
        /* Parition the input arrays */
        while(lo <= hi)
        {
            // Median of both arrays
            mid1=(lo+hi)/2;
            mid2=merge_med-mid1;

            /* Edge Cases */
            // If no elements before the left index, make minimum possible value
            l1=(mid1>0) ? nums1[mid1-1] : Integer.MIN_VALUE;
            l2=(mid2>0) ? nums2[mid2-1] : Integer.MIN_VALUE;
            // If no elements after the right index, make maximum possible value
            r1=(mid1<n) ? nums1[mid1] : Integer.MAX_VALUE;
            r2=(mid2<m) ? nums2[mid2] : Integer.MAX_VALUE;
            // If too far right, go left
            if (l1 > r2)
                hi = mid1-1;
            // If too far left, go right
            else if (l2 > r1)
                lo = mid1+1;
            // If a match is found, return it
            else
                // Return average of the two medians if even merged length
                if((n+m)%2 == 0)
                    return (Math.max(l1,l2)+Math.min(r1,r2))/2.0;
                // Return only one median if odd merged length
                else
                    return Math.max(l1,l2);
        }
        return 0;
    }
}
