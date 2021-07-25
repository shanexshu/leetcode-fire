class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = [gas[i]-cost[i] for i in range(len(gas))]
        
        start = i = 0
        curr = 0
        visited = 0
        while start<len(gas) and visited<len(gas):
            curr += net[i]  # amount after leaving index start
            if curr<0:
                start += 1
                i = start
                curr = visited = 0
                continue
            i = (i+1)%len(gas)
            visited += 1
        
        if visited == len(gas): return start
        return -1
        
        
'''


gas =  [1,2,3,4,5], 

cost = [3,4,5,1,2]

net =  [-2,-2,-2,3,3]
                 s
                 i
         
curr = 0
visited = 5

gas at i+1 = curr + net[i]


sum of net must be >= 0
-2,5,-4,-1,-1,4

4->2->7->1
'''