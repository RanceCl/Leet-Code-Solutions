'''
An integer array, height, with a length of n, is given.
Each integer in the array represents the height of a vertical line. 
The following program is to determine the largest amount of water that could be held by any
combination of the lines, using the x-axis distance with the lines to act as a theoretical
container. 

To do this, I created two pointers that would point to the leftmost and rightmost line in the array, 
finding the area of the current area before incrementing or decrementing the left or right pointer,
respectively, depending on which wall was lower. The currently held maximum area would be compared with
the newly calculated one before storing the largest. This process would continue until the two lines met.

Assumptions:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4

'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPointer,rightPointer,maxArea = 0,len(height)-1,0

        #Loop through the heights until the walls meet. 
        while leftPointer < rightPointer:
            tempArea = self.areaCalculator(rightPointer - leftPointer, height[leftPointer], height[rightPointer])
            
            # Make sure the new area is larger than the currently stored maximum. 
            if tempArea > maxArea: maxArea = tempArea
            
            # Shift left pointer to the right if it is pointing to the lower wall.
            if height[leftPointer] < height[rightPointer]: leftPointer += 1
            
            # Shift right pointer to the left if it is pointing to the lower wall.
            else: rightPointer -= 1
            
        return maxArea

    # Calculates the area of the current container based on the heights of each wall and the distance between them.
    def areaCalculator(self, l, h1, h2):
        # The water level can't be above the lowest wall, so use the lowest wall for the calculation.
        if(h1 < h2): return l * h1
        return l * h2
