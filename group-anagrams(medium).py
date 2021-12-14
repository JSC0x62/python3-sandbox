# https://leetcode.com/problems/group-anagrams/
# https://www.youtube.com/watch?v=vzdNOK2oB2E
# This is O(m * n * 26) 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # This solution uses a HashMap and maps the count for each character to a string
        output = defaultdict(list) 
        
        for s in strs:
            # For each string, need to count the number if each character in it
            # Array is reset after each string (s)
            count = [0] * 26 
            for c in s:
                # counts the number if each character in the string, using a as a refrence point for ASCII values. 
                # For example if b = 81 and a = 80, it gets set to 1 because 81 - 80 = 1
                # And then its incremented by 1 for each time the character appears
                count[ord(c) - ord("a")] += 1 
            
             # If there is another string with the same char count, it will get added to list of values for that string in the map
             # Then the result returns the values, which are pairings of the anagrams
            output[tuple(count)].append(s)
        return output.values()
