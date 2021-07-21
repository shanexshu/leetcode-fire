"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # make a dictionary that maps employee id to employee object
        # get main employee, add value to value of subordinates, recurse
        
        dic = {}
        for emp in employees:
            dic[emp.id] = emp
        
        def imp(emp):
            total = emp.importance
            for sub_id in emp.subordinates:
                sub = dic[sub_id]
                total += imp(sub)
            return total
        
        return imp(dic[id])