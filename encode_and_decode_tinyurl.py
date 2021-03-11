import string
import random
class Codec:

    def __init__(self):
        self.db = {}
        self.length = 6
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        coded = self.genRandomStr(self.length)
        while coded in self.db:
            coded = genRandomStr(self.length)
        self.db[coded] = longUrl
        return coded
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.db:
            return self.db[shortUrl]
        
    
    def genRandomStr(self, length):
        ans = []
        for i in range(length):
            r = random.choice(string.ascii_letters+string.digits)
            ans.append(r)
        return ''.join(ans)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))