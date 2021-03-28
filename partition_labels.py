class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ans = []
        if not S: return ans
        
        last = {}
        for i in range(len(S)):
            last[S[i]] = i
        
        i = 0
        while i<len(S):
            start = i
            end = last[S[i]]
            part = 1
            while i<end and i<len(S):
                i += 1
                part += 1
                end = max(end, last[S[i]])
            ans.append(part)
            i += 1
        return ans