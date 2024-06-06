'''
Given a sorted array of distinct integers and a target value, return the 
index if the target is found. If not, return the index where it would be if 
it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

A simple binary search algorith was used.

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right)//2

            # Target to right, current left half ignored.
            if nums[mid] < target:
                left = mid + 1

            # Target to left, current right half ignored.
            else: 
                right = mid
        return left
