class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = [c for c in s]
        
        for ind in range(len(indices)):
            i = indices[ind]
            source = sources[ind]
            if s[i:i+len(source)] == source:
                ans[i] = targets[ind]
                ans[i+1:i+len(source)] = ['']*(len(source)-1)
                
        return "".join(ans)