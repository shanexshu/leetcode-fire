class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereqs = [0]*numCourses
        post = [[] for _ in range(numCourses)]
        
        for course, pre in prerequisites:
            prereqs[course] += 1
            post[pre].append(course)
        
        todo_stack = []
        ans = []
        
        for i in range(numCourses):
            if prereqs[i]==0:  #no prereqs
                todo_stack.append(i)
        if not todo_stack: return []
        while todo_stack:
            curr_course = todo_stack.pop()
            ans.append(curr_course)
            nextcourses = post[curr_course]
            for nc in nextcourses:
                prereqs[nc] -= 1
                if prereqs[nc]==0:
                    todo_stack.append(nc)
                
        if len(ans)<numCourses:
            return []
        return ans