class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        todo = deque()
        post = [[] for _ in range(numCourses)]
        prereqs = [0]*numCourses
        for c, pre in prerequisites:
            post[pre].append(c)
            prereqs[c] += 1
        
        for i in range(numCourses):
            if prereqs[i]==0:
                todo.append(i)
        ans = 0
        while todo:
            course = todo.popleft()
            ans += 1
            for nc in post[course]:
                prereqs[nc] -= 1
                if prereqs[nc] == 0:
                    todo.append(nc)
        
        return ans==numCourses