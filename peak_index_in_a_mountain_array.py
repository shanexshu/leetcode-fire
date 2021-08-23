class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return [i for i in range(len(arr)) if arr[i]==max(arr)][0]