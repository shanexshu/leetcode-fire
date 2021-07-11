from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [set() for _ in range(numCourses)]
        prereqs = [0]* numCourses
        for a, b in prerequisites:
            adj[b].add(a)
            prereqs[a] += 1
        
        q = deque()
        for i in range(numCourses):
            if prereqs[i]==0:
                q.append(i)
        
        taken = set()
        while q:
            # this should be only courses that have no prereqs left
            course = q.popleft()
            taken.add(course)
            for post in adj[course]:
                prereqs[post] -= 1
                if prereqs[post]==0:
                    q.append(post)
        
        return len(taken)==numCourses