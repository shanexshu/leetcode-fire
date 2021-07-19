class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start
        # for each interval, check if start is before prev end. if so, merge
        # O(nlogn) time
        intervals.sort()
        
        ans = []
        for i in intervals:
            if not ans or i[0]>ans[-1][1]:
                ans.append(i)
            else:
                ans[-1][1] = max(ans[-1][1], i[1])
        
        return ans
    
        # intervals = [[1,3],[2,6],[8,10],[15,18]]
        #                                     i
        # ans = [[1,6],[8,10],[15,18]]