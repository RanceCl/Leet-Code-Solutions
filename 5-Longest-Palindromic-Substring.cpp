/*
Given a string s, the longest panindromic substring within 
s was returned.

The method used was to go through every character in s and 
expand around this center character to find the longest 
palindrome around it. Since the substring could be odd or 
even, this was done twice for each character, once with 
the center being the character at index i, and the second 
time being done with the characters at index i and i+1.

Once this new substring was found, it's length would be  
compared to the currently stored longest substring.

This was repeated until all characters as centers were 
exhausted, with the final substring stored being the 
longest in s. 
*/

class Solution {
public:
    string longestPalindrome(string s) {
        string longPal = "";
        string substringi = "";
        // Loop through every character in string s to use each as a center. 
        for(int i = 0; i < s.length(); i++) {
            // Expand substring twice from 'i', since the palindromic substring could be odd or even
            // Odd Palindrome, one center character at index 'i'.
            substringi = findPalindromeSubstringFromCenter(i, i, s);
            longPal = (substringi.length() > longPal.length()) ? substringi : longPal;
            
            // Even Palindrome, two center characters at indices 'i' and 'i+1'.
            substringi = findPalindromeSubstringFromCenter(i, i+1, s);
            longPal = (substringi.length() > longPal.length()) ? substringi : longPal;
        }

        return longPal;
    }

    // Expand the substring from the center index until the palidrome ends or an edge is reached.
    string findPalindromeSubstringFromCenter(int left, int right, string &s) {
        // Loop will continue until the string's edge is reached or the palindrome ends.
        while(left>=0 && right<s.length() && s[left]==s[right]) {
            left--;
            right++;
        }

        // New palindrome substring
        return s.substr(left+1, right-left-1);
    }
};
