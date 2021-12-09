#https://leetcode.com/problems/maximum-subarray
#https://www.youtube.com/watch?v=5WZl3MMT0Eg&ab_channel=NeetCode
#linear O(n) solution 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #current sum, and the max sum which starts at the first value
        currentSum = 0
        maxSum = nums[0]
        for i in nums:
            #the current sum is increased by itself + the current value, then the max is calculated
            currentSum += i
            maxSum = max(currentSum, maxSum)
            #if the current sum is ever < than 0 it should be reset. This means there is a negative prefix, which will result in a decreasing sum
            if currentSum < 0:
                currentSum = 0
        return maxSum
