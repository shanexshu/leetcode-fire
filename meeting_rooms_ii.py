class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()  # sort by start time
        ans = 0
        in_use = []  # min heap of end times
        latest_end = 0
        for start, end in intervals:
            # either one room opens up or a new room needs to be used
            if in_use:
                earliest = in_use[0]
                if start>=earliest:
                    heapq.heappop(in_use)

            heapq.heappush(in_use, end)

            ans = max(ans, len(in_use))
        return ans
    
    
'''
0 5 10 15 20 25 30
|       |
  |        |
        |  |
'''