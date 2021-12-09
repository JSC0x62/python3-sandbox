#https://leetcode.com/problems/maximum-product-subarray/submissions/
#https://www.youtube.com/watch?v=lXVy6YWFcRM
#One pass O(n) solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Result just needs to be set to something
        #The idea here is that the minumum and max values are both tracked
        #Both are set to 1 as that's a netural number for multiplication
        result = nums[0]
        currentMin = 1
        currentMax = 1
        for i in nums:
            #At each point when passing through the array there are 3 possibilties for both the max and min: 
            #It could be just the current value itself, or it could be that value * the max or the min
            tmpMax = currentMax * i
            currentMax = max(i * currentMax, i * currentMin, i)
            currentMin = min(tmpMax, i * currentMin, i)
            #The result is the max between itself and the max calculated each time
            result = max(result, currentMax)    
        return result
      
      #For example with the array: [2,3,-2,4]:
      #i = 2, currentMax = 2, currentMin = 2, result = 2
      #i = 3, currentMax = 6, currentMin = 3, result = 6
      #i = -2, currentMax = -2, currentMin = -6, result = 6
      #i = 4, currentMax = 4, currentMin = -24, result = 6 
