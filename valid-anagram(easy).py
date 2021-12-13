# https://www.youtube.com/watch?v=9UtInBqnCgA&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=2
# https://leetcode.com/problems/valid-anagram/
# This solution woulld be O(s + t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # one line solution: return sorted(s) == sorted(t)
        #To start with if they arent the same length then they arent anagrams
        if len(s) != len(t):
            return False
        
        # A map that is basically a str : int 
        # meaning the character : amount of times it appears
        sCount = {}
        tCount = {}
        
        #Loop through the string
        for i in range(len(s)):
            # What this is does is for the current value in the string ([s[i]), increment it in the map by 1, and if its not there the defualt value starts it at 0
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
        # Now both hashmaps have been created. Each have the characters and the amount of times they appear in the string
        for c in sCount:
            # The hashmaps should be the same, if any values are different they are not anagrams
            if sCount[c] != tCount.get(c, 0):
                return False
        
        return True
