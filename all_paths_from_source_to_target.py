class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = deque()
        q.append([0, []])
        ans = []
        
        while q:
            todo = q.popleft()
            num, path = todo
            if num == len(graph)-1:
                ans.append(path + [num])
            for edge in graph[num]:
                q.append([edge, path + [num]])
        
        return ans