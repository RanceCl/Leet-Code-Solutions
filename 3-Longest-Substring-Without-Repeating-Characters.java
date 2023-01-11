/* 
This function takes in a string of characters and finds the character length of longest substring without a repeating character. This would be done by reading 
in the characters of the input string and counting the substring length as well as indicating that said character was encountered. 

A sliding window method was used for this purpose. The code would use a while loop to increment the rightmost bound of the window and indicate that they have been
visited. Once a repeat was encountered, the code would determine the length of the current substring using the window size. It would proceed to indicate that all
characters within the window before the encountered variable hadn't been encountered while incrementing the left window boundary. 

An 128 integer long array was used to hold the number of each character that was encountered, with each index corresponding to the integer value of a 
character (a=97,b=98,c=99,...).
*/

class Solution {
    public int lengthOfLongestSubstring(String s) {
        // The sWindow variable will hold the window
        String sWindow = "";
        int longestLength=0;

        /* Loop through the string to count the substring lengths */
        for(char ch: s.toCharArray())
        {
            /* If the current character is already in the window, shift the window */
            if(sWindow.contains(String.valueOf(ch)))
            {
                //Shift window to be after the repeated character
                if(sWindow.contains(String.valueOf(ch)))
                    sWindow = sWindow.substring(sWindow.indexOf(String.valueOf(ch))+1);
            }
            sWindow = sWindow + ch;                                     // Add the current character to the window
            longestLength = Math.max(longestLength, sWindow.length());
        }
        return longestLength;
    }
}
