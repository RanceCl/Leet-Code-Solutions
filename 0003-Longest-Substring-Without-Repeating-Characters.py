''' 
This function takes in a string of characters and finds the character length of longest substring without a repeating character. This would be done by reading 
in the characters of the input string and counting the substring length as well as indicating that said character was encountered. 
A sliding window method was used for this purpose. The code would use a while loop to increment the rightmost bound of the window and indicate that they have been
visited. Once a repeat was encountered, the code would determine the length of the current substring using the window size. It would proceed to indicate that all
characters within the window before the encountered variable hadn't been encountered while incrementing the left window boundary. 
An 128 integer long array was used to hold the number of each character that was encountered, with each index corresponding to the integer value of a 
character (a=97,b=98,c=99,...).
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # The sWindow variable will hold the window
        sWindow = ""
        longestLength=0

        if(len(s)==0):
            return 0
        elif(len(s)==1):
            return 1
        
        # Loop through the string to count the substring lengths
        for ch in s:
            # If the current character is already in the window, shift the window
            if(ch in sWindow):
                sWindow = sWindow[(sWindow.index(ch)+1):]

            # Add the current character to the window
            sWindow = sWindow + ch
            longestLength = max(longestLength, len(sWindow))
        
        return longestLength
