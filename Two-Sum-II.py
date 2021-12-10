#
# https://www.youtube.com/watch?v=cQ1Oz4ckceM&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=4&ab_channel=NeetCode
# Simple O(n) solution with a binary search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l <= r:
            #Basically just do a binary search and increment the left is the sum isnt enough, and decrement the right if its too large
            if numbers[l] + numbers[r] == target:
                #("1 indexed" meaning it starts from 1 instead of 0. So just have to increase each value by 1)
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return []
