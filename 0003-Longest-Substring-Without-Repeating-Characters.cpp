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
public:
    int lengthOfLongestSubstring(string s) {
        // CharCount holds the count for all 128 chars of the current substring.
        bool CharCount[128] = {false};
        int windLeft=0, windRight=0;
        int longestLength=0;
         
        /* Loop through the string to count the substring lengths */
        for(windRight=0; windRight<s.size(); windRight++)
        {
            /* If the current character at the index of the current right boundary hasn't been encountered before, indicate it has been encountered */
            if(CharCount[s[windRight]] == false)
                CharCount[s[windRight]] = true;           // The character's integer value corresponds to its index
            
            /* If the current character has already been encountered, shift the left window boundary */
            else
            {
                // Compare the longest substring length with the current substring length
                longestLength = max(longestLength, (windRight - windLeft));

                /* Shift the left window boundary up to the point of the repeated character */
                // Mark all characters before the repeated character as unvisited
                while(CharCount[s[windRight]] != false)
                {
                    CharCount[s[windLeft]] = false;
                    windLeft++;
                }
                CharCount[s[windRight]] = true;  //Repeated character must be set back to true at the end of the loop
            }
        }
        longestLength = max(longestLength, (windRight - windLeft));
        
        return longestLength;
    }
};
