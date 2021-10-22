class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        s_list = list(s)
        s_list.sort()
        s_list.sort(key=lambda x: freq[x], reverse=True)
        return "".join(s_list)