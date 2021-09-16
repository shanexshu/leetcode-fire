class Solution:
    def isValid(self, s: str) -> bool:
        openPara = []
        match = {'(':')','{':'}', '[':']'}
        for c in s:
            if c in '([{':
                openPara.append(c)
            else:
                if not openPara: return False
                if match[openPara.pop()] != c:
                    return False
        return len(openPara)==0