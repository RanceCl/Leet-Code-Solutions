'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Assumptions:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #print(strs, strs[1], strs[1][1])
        i = 0

        # Find the length of the smallest string in the list
        minL = self.smallestLength(strs)
        
        # The most the loop should ever go is up to the end of the smallest string.
        while i < minL:
            # Compare the characters at the index for each string.
            for s in strs[1:]:
                if s[i] != strs[0][i]: 
                    return s[:i]
            i += 1
        # Used in the instance that an entire string is a match. 
        return strs[0][:i]

    #Find the length of the smallest string in an array of strings.
    def smallestLength(self, strs) -> int:
        # Make sure that the array isn't empty
        if len(strs) == 0:
            return 0
        minL = len(strs[0])

        # Find the smallest length
        for s in strs[1:]:
            if minL > len(s):
                minL = len(s)
        return minL
        
