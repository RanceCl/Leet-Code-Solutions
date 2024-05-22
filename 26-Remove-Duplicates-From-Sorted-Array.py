'''
Given an integer array nums sorted in non-decreasing order, remove 
the duplicates in-place such that each unique element appears only 
once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get 
accepted, you need to do the following things:
    Change the array nums such that the first k elements of nums 
    contain the unique elements in the order they were present in 
    nums initially. The remaining elements of nums are not important 
    as well as the size of nums.
    
    Return k.

Assumptions: 
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            # Overwrite next non-unique value with the next unique value.
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
