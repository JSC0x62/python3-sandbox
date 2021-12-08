# https://leetcode.com/problems/contains-duplicate/submissions/
# https://www.youtube.com/watch?v=3OamzN90kPg&ab_channel=NeetCode
#Simple one pass O(n) time solution 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Sets cant have duplicates
        setNums = set()
        for i in nums:
            #if its in the set, then a duplicate value was found. return true
            if i in setNums:
                return True
            #keep adding values to the set until a duplicate is found
            setNums.add(i)
        #No duplicates found
        return False
