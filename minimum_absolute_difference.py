class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sortedArr = sorted(arr)
        ans = []
        
        minDist = math.inf
        for i in range(1,len(sortedArr)):
            minDist = min(minDist, sortedArr[i]-sortedArr[i-1])
        
        for i in range(1,len(sortedArr)):
            if sortedArr[i]-sortedArr[i-1] == minDist:
                ans.append([sortedArr[i-1],sortedArr[i]])
        
        return ans