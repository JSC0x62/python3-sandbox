# Two sum, O(n) solution, one pass
# https://www.youtube.com/watch?v=KLlXCFG5TnA&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap for keeping track of value of visited elements and their index, pair is value : index
        found = {}
        #main loop, current index and value incremented automatically
        for index, value in enumerate(nums): 
            #this is the value we need, does it exist?
            x = target - nums[index]
            if x in found:
                #returns back the indecies of the pair
                return [found[x], index]
            else:
                #if not add this pair to the map
                found[value] = index
       
        return found
