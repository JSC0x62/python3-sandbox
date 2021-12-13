# https://www.youtube.com/watch?v=44H3cEC2fFM&ab_channel=NeetCode
# https://leetcode.com/problems/merge-intervals
# O(n log n) solution


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # first, each interval (which is an array of 2 ints) are sorted by the first element in each one
        # .sort() may do this automatically 
        intervals.sort(key = lambda i : i[0])
        # Where the result will be stored, first value is set to the first in the input list
        output = [intervals[0]]
        
        # Starts at 1 (second element), and start and end are the first and second values in each array
        for start, end in intervals[1:]:
            print("start: ", start, "end: ", end)
            # This is the end of the previous interval. [1] is the second (end) element in the previous array [-1]
            lastEnd = output[-1][1]
            print(output[-1][1])
            
            #In this case there is overlap. So it sets the end to the bigger value, and now the intervals are merged
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
                # for example: [1, 5] [2, 4] = [1, 5]
            else:
                output.append([start, end])
        return output
