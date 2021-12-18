# https://leetcode.com/problems/container-with-most-water/
# https://www.youtube.com/watch?v=UuiTKBwPgAo
# O(n) solution, uses binary search
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # binary search so it has left and right pointers starting from start and end
        l = 0
        r = len(height) - 1
        #used for computing the area
        maxArea = 0
        currentArea = 0
        
        # go until they meet
        while l < r:
            # Area is computed by taking the distance of the pointers and multiplying by the smallest height of them
            # Smallest because water would "fall out" if they are uneven
            currentArea = (r - l) * min(height[r], height[l])
            # Keep track of what the max area is
            maxArea = max(maxArea, currentArea)
            # If the left pointer is < than the right, increment the left
            if height[l] < height[r]:
                l += 1
            # IF the opposite is true, decrement the right. If they were equal you could go either way, so can just leave it like this with the right pointer.  
            else:
                r -= 1
        return maxArea
