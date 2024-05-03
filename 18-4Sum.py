'''
An array of integers was given with the intention of returning all 
quadruplets 
    [nums[a], nums[b], nums[c], nums[d]]

such that: 
    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

Notice that the solution set must not contain duplicate quadruplets.

To solve this problem, a generic method to find the k-sum of a set of
numbers was designed, with the intention of using this to find the 
desired 4-sum with the desired target value.

Assumptions: 
1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9

'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.kSum(nums, 4, target)

    # Method that starts the kSum algorithm
    def kSum(self, nums, k, target):
        nums.sort()
        
        # Initialize the recursive loop
        return self.kSumLoop(nums, k, target)
        
    # Recursive loop to find every unique set of values that will equal the target
    def kSumLoop(self, nums, k, target):
        res = []

        # Base case for k-sum, the 2-sum
        if k == 2: return self.twoSumII(nums, target)
        
        for i in range(len(nums)):
            # Skip duplicate values encountered
            if i > 0 and nums[i] == nums[i-1]: continue
            
            solns = self.kSumLoop(nums[i+1:], k-1, target - nums[i])
            # Append the previous values for the sum to the 2-sum found
            for soln in solns:
                res.append([nums[i]]+soln)
        return res
            
    # Method to find the 2-sum for a list of numbers and a target
    def twoSumII(self, nums, target):
        res = []
        # Initialize the pointers for both ends of the list
        l, r = 0, len(nums)-1

        # Loop through the list to find the addends
        while(l<r):
            # Current sum is smaller than target, increase lower addend
            if nums[l] + nums[r] < target: l+=1
            # Current sum is larger than target, decrease higher addend
            elif nums[l] + nums[r] > target: r-=1
            # When an answer is found: 
            else:
                res.append([nums[l], nums[r]])
                l +=1
                # Keep incrementing if duplicates are still found
                while l<r and nums[l] == nums[l-1]: l +=1
        return res
