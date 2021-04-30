class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots = slots1[:] + slots2[:]
        slots.sort()
        first = 0
        second = 1
        
        while second<len(slots):
            start, end = slots[first]
            nstart, nend = slots[second]
    
            if nstart<end:
                diff = min(end, nend) - nstart
                if diff>=duration:
                    return [nstart, nstart+duration]
                second += 1
            else:
                first += 1
                if first==second: second += 1
                            
        return []