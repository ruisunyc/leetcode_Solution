class Codec:
    def __init__(self):
        self.dic = {}
    def getkey(self):
        return ''.join(random.sample(string.ascii_letters+string.digits,6))
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.getkey()
        while key in self.dic:
            key = self.getkey()
        self.dic[key] = longUrl
        return 'http://tinyurl.com/'+key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dic.get(shortUrl.replace('http://tinyurl.com/',''))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))