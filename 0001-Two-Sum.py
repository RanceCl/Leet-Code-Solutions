''' 
This function takes in an array of integers and a target sum and find the two integers that will add together into the sum.
The indices of these two numbers would be returned in a vector.
This was done by 
Time Complexity: O(NlogN)
Space Complexity: O(N)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1=0
        index2=len(nums)-1
        # Copy the input array and sort it
        nums_sorted = nums.copy()
        nums_sorted.sort()

        # Loop through the vector to find the addends 
        while(index1<index2):
            #If the addends equal the target, exit the while loop 
            if ((nums_sorted[index1]+nums_sorted[index2]) == target):
                break
            #If the current numbers are smaller than the target, the lower addend must be increased
            elif ((nums_sorted[index1]+nums_sorted[index2]) < target):
                index1+=1
            #If the current numbers are larger than the target, the higher addend must be decreased
            else:
                index2-=1

        # Find the original indices of the addend values
        addend1 = nums.index(nums_sorted[index1])
        addend2 = nums.index(nums_sorted[index2])

        # Make sure the indexes aren't duplicates. This is mostly necessary in case both addends are the same
        if addend1==addend2:
            addend2 = nums.index(nums_sorted[index2],addend1+1)

        #Make sure the lowest index is returned first
        if addend1 < addend2:
            return [addend1, addend2]
        else:
            return [addend2, addend1]
