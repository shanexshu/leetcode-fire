class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for char in '!?,;.\'':
            paragraph = paragraph.replace(char, ' ')
        words = paragraph.split()
        counts = defaultdict(int)
        ma = 0
        ans = ""
        bannedset = set(banned)
        for word in words:
            lower = word.lower()
            if lower not in bannedset:
                counts[lower] += 1
                if counts[lower] > ma:
                    ans = lower
                    ma = counts[lower]
        print(counts)
        return ans