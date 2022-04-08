class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = sorted(nums, reverse=True)[:k]
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

'''
8554

just need the store the first k
and then report the min
can use a heap
'''