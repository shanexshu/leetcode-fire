class Solution:
    def __init__(self):
        self.encodedAnagrams = set()
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for string in strs:
            encoded = self.encodeAnagram(string)
            if encoded not in groups:
                groups[encoded] = []
            groups[encoded].append(string)
            
        return groups.values()
        
    def encodeAnagram(self, anagram: str):
        encoded = [0]*26
        for char in anagram:
            index = ord(char)-ord('a')
            encoded[index] += 1
        return tuple(encoded)