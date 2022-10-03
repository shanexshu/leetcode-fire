class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalTime = 0
        start = 0
        maxTime = neededTime[0]
        colorTimeSum = neededTime[0]
        
        for i in range(1, len(colors)):
            if colors[i] == colors[start]:
                maxTime = max(maxTime, neededTime[i])
                colorTimeSum += neededTime[i]
            else:
                if i-start>1:
                    totalTime += colorTimeSum - maxTime
                start = i
                maxTime = neededTime[i]
                colorTimeSum = neededTime[i]
        
        i = len(colors)
        if i-start>1:
            totalTime += colorTimeSum - maxTime

                
        return totalTime
        