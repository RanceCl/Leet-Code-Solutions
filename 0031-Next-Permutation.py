'''
A permutation of an array of integers is an arrangement of its members 
into a sequence or linear order.

The next permutation of an array of integers is the next lexicographically 
greater permutation of its integer. If such arrangement is not possible, 
the array must be rearranged as the lowest possible order (i.e., sorted in 
ascending order).

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

There is a pattern to finding the next permutation: 
Starting from the back, we must look for first digit that is not in a 
descending pattern. This digit is our pivot that will be changed. To make 
the next permutation (next number larger than the current), the pivot must 
be swapped with the smallest number in the descending pattern that is 
greater than the pivot (its rightmost successor in the suffix). This will 
put the numbers in the descending pattern in the right order for them to be 
reversed. Reversing the descending patter will finally give the next 
permutation.

Assumptions: 
1 <= nums.length <= 100
0 <= nums[i] <= 100
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swapPtr = len(nums) - 1
        # The pivot will at least be in front of the last digit
        pivotPtr = swapPtr - 1

        # Find index of first not increasing number from the back
        while pivotPtr >= 0 and (nums[pivotPtr] >= nums[pivotPtr+1]):
            pivotPtr -= 1
        
        # If the beginning is reached, then no larger permutation exists
        if pivotPtr < 0:
            nums.reverse()
            return

        # Find the first number greater than the pivot from the back
        while nums[swapPtr] <= nums[pivotPtr]:
            swapPtr -= 1
            
        # Swap pivot with the number that it needs to be traded for
        nums[pivotPtr], nums[swapPtr] = nums[swapPtr], nums[pivotPtr]

        # Reverse the descending pattern encountered
        nums[pivotPtr+1:] = reversed(nums[pivotPtr+1:])
