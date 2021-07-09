class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        def visit(room):
            if room not in visited:
                visited.add(room)
                keys = rooms[room]
                for key in keys:
                    visit(key)
        
        visit(0)
        return len(visited)==len(rooms)