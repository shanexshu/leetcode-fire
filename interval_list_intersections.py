class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        i = j = 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
            if start1<=start2<=end1 or start2<=start1<=end2:
                ans.append([max(start1,start2), min(end1,end2)])
            if end1<=end2:
                i += 1
            if end2<=end1:
                j += 1

        return ans
        
        
'''
0,2;5,10

1,5;8,12


'''