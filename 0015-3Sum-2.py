'''
An array of integers was given with the intention of returning all 
triplets 
    [nums[i], nums[j], nums[k]] 

such that: 
    i != j, i != k, and j != k, and 
    nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Assumptions: 
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        numsLen = len(nums)
        triples = set()
        
        # Two sum
        for i in range(numsLen-2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]: 
                continue

            x = nums[i]
            # Two pointers from each side of the list
            j = i+1
            k = numsLen-1

            while j < k:
                # x + y + z = 0 --> z = -x + -y
                y, z = nums[j], nums[k]
                currSum = x + y + z

                # Close in until a new potential 0 sum is found.
                if currSum > 0: 
                    k -= 1
                elif currSum < 0: 
                    j += 1
                else:
                    triples.add((x,y,z))
                    j, k = j+1, k-1
                    # Skip duplicates
                    while j < k and nums[j] == nums[j-1]: 
                        j += 1
                    while j < k and nums[k] == nums[k+1]: 
                        k -= 1
        return triples
