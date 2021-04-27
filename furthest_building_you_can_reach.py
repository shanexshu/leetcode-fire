import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        climbsdone = []
        heapq.heapify(climbsdone)
        n = len(heights)
        
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff>0:
                
                if ladders>0:
                    ladders -= 1
                    heapq.heappush(climbsdone, diff)
                else:
                    if not climbsdone or diff<climbsdone[0]:
                        bricks -= diff
                    else:
                        bricks -= heapq.heappop(climbsdone)
                        heapq.heappush(climbsdone, diff)
                    if bricks<0: return i
        
        return n-1