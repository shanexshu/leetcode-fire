class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # graph
        
        def getSyns(word, seen=set()):
            seen.add(word)
            for syn in graph[word]:
                if syn not in seen:
                    getSyns(syn, seen)
            return seen
        
        graph = defaultdict(list)
        groups = {}
        for a,b in synonyms:
            graph[a].append(b)
            graph[b].append(a)
        
        for word in text.split(" "):
            if word in graph:
                groups[word] = list(getSyns(word,set()))
                groups[word].sort()
            
        ans = []
        words = text.split()
        curr_sent = []
        
        def generate(i):
            nonlocal ans
            if len(curr_sent)==len(words):
                ans.append(" ".join(curr_sent))
                return
            if words[i] not in groups:
                curr_sent.append(words[i])
                generate(i+1)
                curr_sent.pop()
            else:
                for syn in groups[words[i]]:
                    curr_sent.append(syn)
                    generate(i+1)
                    curr_sent.pop()
                    
        generate(0)
        return ans