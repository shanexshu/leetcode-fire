class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        i = 0
        while i<len(strs[0]):
            char = strs[0][i]
            for s in strs[1:]:
                if len(s)<=i or s[i]!=char:
                    return "".join(ans)
            ans.append(char)
            i += 1
        return "".join(ans)