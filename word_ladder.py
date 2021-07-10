class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if len(beginWord)!=len(endWord): return 0
        words = set(wordList)
        if endWord not in words: return 0
        
        q = deque()
        q.append((beginWord, 1))
        seen = set()
        while q:
            word, depth = q.popleft()
            
            if word == endWord:
                return depth
            
            for replace in range(len(word)):
                for i in range(26):
                    c = chr(ord('a') + i)
                    new_word = word[:replace] + c + word[replace+1:]
                    if new_word in words and new_word not in seen:
                        seen.add(new_word)
                        q.append((new_word, depth+1))
                        
            
        return 0