# https://leetcode.com/problems/product-of-array-except-self/submissions/
# https://www.youtube.com/watch?v=bNvIQI2wAjk
# The idea is every value in the array, needs to be multiplied by every other number, except itself whihc results in an array 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # a new array for storing the result
        res = [1] * len(nums)
        prefix = 1
        postfix = 1
        
        # calculate the prefixes first
        for i in range(len(nums)):
            #set value in the result array to the prefix
            res[i] = prefix
            # prefix is just itself * current value in nums array
            prefix *= nums[i]
        # work backwards through postfix array
        for i in range(len(nums) - 1, -1, -1):
            # update each value in the result array starting from the end. Its just itself * the postfix
            res[i] *= postfix
            # post is calculated basically the same as prefix
            postfix *= nums[i]
        return res
