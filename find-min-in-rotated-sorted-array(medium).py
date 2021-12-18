# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# https://www.youtube.com/watch?v=nIVW4P8b1VA&ab_channel=NeetCode
# this is a O(log n) solution as required
class Solution:
    def findMin(self, nums: List[int]) -> int:
       # Sort of a minary search, uses a left, right and middle pointer
        l = 0
        r = len(nums) - 1
        result = nums[0]
        
        while l <= r:
            # In this case the array is sorted, so the left will be the smallest value
            if(nums[l] < nums[r]):
                result = min(nums[l], result)
                break
            # Calculate the middle point
            mid = (l + r) // 2
            # Update the result
            result = min(nums[mid], result)
            # In this case, we're in the left sorted portion, and the min is going to be somewhere in the right
            if nums[mid] >= nums[l]:
                l = mid + 1
            # Otherwise, go left
            else:
                r = mid - 1
        return result
            
