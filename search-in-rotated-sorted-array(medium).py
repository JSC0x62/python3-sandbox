#https://www.youtube.com/watch?v=U8XENwh8Oy8
#https://leetcode.com/problems/search-in-rotated-sorted-array
#O log(n) solution using binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
           # 2 pointers for start and end of the array
        l = 0
        r = len(nums) - 1
        
        # perform a binary search
        while l <= r:
            #the middle value in the portion of the array being searched
            mid = (l + r) // 2
            #if the mid = target, then the search is done
            if target == nums[mid]:
                return mid
            
            #This checks to see if its in the left sorted portion (before the pivot index)
            if nums[l] <= nums[mid]:
                #in this case the target is somewhere in the right portion, so search there
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                #if not, then its in the left portion, so search there
                else:
                    r = mid - 1
            #If not in the left portion, then its in the right
            else:
                #in this case, its somewhere in the left portion so search there
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                #if not, its in the right portion so search there
                else:
                    l = mid + 1
                #process continues until target is found
        return -1     
