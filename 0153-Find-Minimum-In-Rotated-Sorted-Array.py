'''
Suppose an array of length n sorted in ascending order is rotated between 
1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time 
results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum 
element of this array.

You must write an algorithm that runs in O(log n) time.

We want to use binary search to narrow in on the minimum, though due to the 
rotation of the array, it is no longer in ascending order. There are still 
some rules that we can use, however.

Because of the array being rotated, there will be a single pivot point 
where the numbers go from increasing to descreasing. (There is a chance of 
no pivot point existing, if the rotation ends with the entire array in its 
original state.) The minimum value will either be beginning or the number 
right after the pivot point.

If the value at the current middle point is larger than what's on the 
right, that means that the middle is located to the left of the pivot 
point (and thus, to the left of the minimum). Since we know that the 
minimum isn't in the left half of the list, we can make our new left 
value to be 1 more than the current middle. 

If the value at the current middle point is smaller than what's on the 
right, that means that the middle is located to the right of the pivot 
point (and thus, to the right of the minimum). Since we know that the 
minimum isn't in the right half of the list, we can make our new right 
value to be equal to the current middle. 

For each loop, the left and right with narrow in on the minimum value until 
they are both equal to the same index, the index of the minimum value. 

Assumptions: 
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        # When the two are the same point, they are at the minimum.
        while left < right:
            mid = (left+right)//2

            # Middle to left of pivot point, current left half ignored.
            if nums[mid] > nums[right]:
                left = mid + 1

            # Middle to right of pivot point, current right half ignored.
            else:
                right = mid
        return nums[left]
