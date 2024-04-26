'''
An array of integers, nums, along with a target integer, target, 
are given with the intention of finding three integers in nums
where the sum is closest to the target. This closest sum is what
is returned.

Assumptions: 
3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4

'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        numsLen = len(nums)
        dist = float('inf')
        
        # Two sum
        for i in range(numsLen-2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]: continue

            # Two pointers from each side of the list
            j = i+1
            k = numsLen-1

            while j < k:
                # target = x + y + z
                currSum = nums[i] + nums[j] + nums[k]

                if currSum == target:
                    return target
                elif abs(target-currSum)<dist:
                    dist = abs(target-currSum)
                    finalSum = currSum
                
                # Close in until a new potential sum is found.
                if currSum > target: k -= 1
                elif currSum < target: j += 1
        
        return finalSum
