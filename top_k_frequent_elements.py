class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        topFreq = []
        for num in nums:
            frequencies[num] += 1
        heap = [(-frequencies[num], num) for num in frequencies.keys()]
        heapq.heapify(heap)
        
        for _ in range(k):
            _, num = heapq.heappop(heap)
            topFreq.append(num)
            
        return topFreq