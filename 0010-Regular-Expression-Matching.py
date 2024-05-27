'''
Given an input string s and a pattern p, implement regular expression 
matching with support for '.' and '*' where:
    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.
    ('.*' Matches zero or more of any character. The character 
    doesn't have to be the same)
The matching should cover the entire input string (not partial).

This was doing a recursive depth first search function. 

Dynamic programming was utilized as well, with all previously 
calculated results for combinations of pointers being stored in 
a memoization dictionary. 

Whenever a result was calculated for a combination of pointers for 
the inputs, this result would be stored. Since pointers may be 
compared multiple times, storing results in the cache would allow 
us to simply return previously calculated results instead of 
repeating them.

A few edge cases were made at the start: 
    The first was to check to see if the current combination of 
    pointers had already been checked. Returning the previously 
    calculated result if it had been.

    The second was one checking if the end of both inputs had been 
    reached. If both had entirely been checked without error, that 
    meant that they matched. 

    The third checked if the pattern's end had been reached before 
    the string. In such a case, the two couldn't be a match. 
    
    No edge case for the string alone was required since the string's
    end could be reached before the pattern's. If the pattern ended 
    with a star but the string didn't use it, then the string's end 
    would be reached without the pattern's end being reached. 

After these, the current character being pointed to for each input 
was checked to see if they matched. It would count as a match if the 
current character of the pattern was the '.', since it could be any.

The character after the current pattern one was checked to see if it 
was a '*'. It if was, then the dfs function would be called twice: 
    1. The case in which the star was found but not used:
        The pointer for s didn't need to be incremented, since a 
        character before a star didn't have to be used. 
        
        Since pattern's character points to the character before the
        star, its pointer would be incremented by 2 to skip the star
        to the next character.
    
    2. The case where the star was found and used (if matching):
    (This would only occur if match was previously found to be true
    since it CAN'T be used if the pointed to characters for both are 
    the same.)
        The pointer for s would be incremented by one since it needs 
        to be compared to p's current character to determine if the 
        star is still being used. 

        The pointer for p didn't need to be incremented since s's 
        character needs to be compared to p's current character.
Both cases needed to be tested, since it was possible for s's 
character to be the same as one from a star, while also not being
the result of the star itself. 

As an example, let's use s = aaaaa; p = a*a
We can't assume that every 'a' in s is a result of the star, since 
there can 'a's that aren't because of it. If the code simply assumes 
that every 'a' in s is a result of the '*', then it would mark the 
two as not matching. So, the code needs to check for both cases.

If no star was encountered, but the two characters matched, then both
pointers simply need be incremented by one to compare the next.

If the end of the function was reached, that meant that the 
comparison (at least for this series of cases) showed the two to not 
match, returning false. 

Assumptions:
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will
be a previous valid character to match.
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Memoization will be used so we don't need to repeat 
        memoTable = {}

        def dfs(sPtr, pPtr):
            # If current pointer combo already computed, return result.
            if (sPtr, pPtr) in memoTable: 
                return memoTable[(sPtr, pPtr)]
            
            # If both inputs' ends are reached, they've matched perfectly.
            if sPtr >= len(s) and pPtr >= len(p):
                return True
            # If pattern's end reached before string's, they aren't the same.
            if pPtr >= len(p):
                return False
            
            # Check if there's a match between the character at each index 
            match = sPtr < len(s) and (s[sPtr] == p[pPtr] or p[pPtr] == ".")

            # Check if the pattern's next character is a *
            if (pPtr+1) < len(p) and p[pPtr + 1] == "*":
                # Test for both the star being used and not used. 
                memoTable[(sPtr, pPtr)] = (
                    # Star not used; skip the next character, which is '*'.
                    dfs(sPtr, pPtr+2) or 
                    # Star used; only possible if match is true.
                    (match and dfs(sPtr+1, pPtr))
                )
                return memoTable[(sPtr, pPtr)]

            # When no star is involved, simply increment to the next character for each. 
            if match:
                memoTable[(sPtr, pPtr)] = dfs(sPtr+1, pPtr+1)
                return memoTable[(sPtr, pPtr)]
            
            # If this part is reached, the two can't be matches
            memoTable[(sPtr, pPtr)] = False
            return memoTable[(sPtr, pPtr)]
        
        return dfs(0,0)
