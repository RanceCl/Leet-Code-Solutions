/* 
This function takes in an array of integers and a target sum and find the two integers that will add together into the sum.
The indices of these two numbers would be returned in a vector.

In order to make the code faster, inputs were sorted so the code could iterate from the beginning and end.

Assume that each vector and target will have exactly one solution.

Time Complexity: O(NlogN)
Space Complexity: O(N)
*/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] nums_sorted = nums.clone();
        int[] addends = new int[2];
        int i, j=0;
        int index1=0, index2=nums.length-1;

        // Sort the copy of the input integer array
        Arrays.sort(nums_sorted);

        /* Loop through the vector to find the addends */
        while(index1<index2)
        {
            //If the addends equal the target, exit the while loop 
            if( (nums_sorted[index1]+nums_sorted[index2]) == target )
                break;
            //If the current numbers are smaller than the target, the lower addend must be increased
            else if( (nums_sorted[index1]+nums_sorted[index2]) < target )
                index1++;
            //If the current numbers are larger than the target, the higher addend must be decreased
            else
                index2--;
        }

        /* Find the original indices of the addend values */
        for(i=0; i<nums_sorted.length; i++)
        {
            //copy the original index to the addend to the array to be returned
            if( (nums_sorted[index1] == nums[i]) || (nums_sorted[index2] == nums[i]) )
            {
                addends[j]=i;
                j++;                    //j is used to make sure that the first encountered addend index is first
            }
        }

        return addends;
    }
}
