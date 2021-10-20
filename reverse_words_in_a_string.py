class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join([word for word in reversed(words) if word!= ""])