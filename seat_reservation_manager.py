class SeatManager:

    def __init__(self, n: int):
        self.unreserved = [i+1 for i in range(n)]
        heapq.heapify(self.unreserved)

    def reserve(self) -> int:
        return heapq.heappop(self.unreserved)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

'''
option 1
list of booleans - list[i] = reserved or not
- reserve: find the smallest unreserved by scanning list, O(n)
- unreserve: O(1)

option 2
list of 
min heap of unreserved seats
- reserve: O(log n)
- unreserve: O(log n)

'''