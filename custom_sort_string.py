from collections import defaultdict
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        ordervals = defaultdict(int)
        for i, c in enumerate(order):
            ordervals[c] = i
        ans = list(str)
        ans.sort(key=lambda x:ordervals[x])
        return "".join(ans)