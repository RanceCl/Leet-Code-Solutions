'''
There is an integer array nums sorted in ascending order 
(with distinct values).

Prior to being passed to your function, nums is possibly rotated at an 
unknown pivot index k (1 <= k < nums.length) such that the resulting array 
is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] 
(0-indexed). 

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become 
[4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


We want to use binary search to narrow in on the target, though due to the 
rotation of the array, it is no longer in ascending order. There are still 
some rules that we can use, however.

Because of the array being rotated, there will be a single pivot point 
where the numbers go from increasing to descreasing. (There is a chance of 
no pivot point existing, if the rotation ends with the entire array in its 
original state.) 

Since everything before and after this pivot point ARE properly sorted, 
that means that there will also be two halves of the list. 
    The half with the pivot. This will not be perfectly sorted, due to the 
    single jump.

    The perfectly sorted half. Without the pivot, it will have no part that
    are decreasing.

If the value at the current middle point is larger than what's on the 
right, that means that the middle is located to the left of the pivot. 

If the value at the current middle point is smaller than what's on the 
right, that means that the middle is located to the right of the pivot.

The side of the middle that is opposite to the pivot is perfectly sorted.

Therefore, 
(m > r) = m is left of pivot =  | Sorted Half | m | Pivot Half  |
(m < r) = m is right of pivot = | Pivot Half  | m | Sorted Half |

Now that we know these rules, we can more accurately scan through the list. 

We can very easily check if the target is in the range of the sorted half. 
    If the target is in the sorted half, 
    then we can ignore the not sorted half.

    If the target isn't in the sorted half, 
    then it must be in the not sorted half.


For each loop, we check if the middle is the current target. If the left and
the right pointer end up meeting without a target being found, then the 
target must not be present.


Assumptions: 
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid

            # Middle to left of pivot point, all before middle is sorted
            if nums[mid] > nums[right]:
                # Target in left half, current right half ignored.
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Target in right half, current left half ignored.
                else: 
                    left = mid + 1
                
            # Middle to right of pivot point, all after middle is sorted
            else:
                # Target in right half, current left half ignored.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Target in left half, current right half ignored.
                else: 
                    right = mid - 1
        return -1
        
