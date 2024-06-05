'''
Given an array of integers nums sorted in non-decreasing order, find the 
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

This was done using a binary search algorithm, with a simple adjustment. 
The search would continue after the initial target had been found, updating 
the value to be returned each time. 

Depending of if we wanted the lowest or the highest index, the function 
would:
    Lowest wanted: Every time target found, adjust right value to search
    lower indexes for target.

    Highest wanted: Every time target found, adjust left value to search
    larger indexes for target.

Once the end of the loop was reached, it would return the final recorded 
index for the target value. 

Assumptions:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [
            self.binarySearch(nums, target, True), # Starting position 
            self.binarySearch(nums, target, False) # Ending position
            ]
        
    # Search for the lowest or highest index for the target value
    def binarySearch(self, nums, target, lookForLowIndex):
        left, right = 0, len(nums)-1
        ans = -1
        while left <= right:
            mid = (left+right)//2

            # Target to right, current left half ignored.
            if nums[mid] < target:
                left = mid + 1

            # Target to left, current right half ignored.
            elif nums[mid] > target:
                right = mid - 1
            
            # Target found
            else: 
                ans = mid
                # Looking for lower index, ignore right half
                if lookForLowIndex:
                    right = mid - 1
                # Looking for upper index, ignore left half
                else:
                    left = mid + 1
        return ans
            
