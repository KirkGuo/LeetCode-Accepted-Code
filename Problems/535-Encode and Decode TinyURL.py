class Codec:
    def __init__(self):
        self.url2tiny = {}
        self.tiny2url = {}
        self.cnt = 0
        
    def encode(self, longUrl):
        if longUrl in self.url2tiny:
            return self.url2tiny[longUrl]
        else:
            tmp = 'http://tinyurl.com/{}'.format(self.cnt)
            self.url2tiny[longUrl] = tmp
            self.tiny2url[tmp] = longUrl
            self.cnt += 1
            return tmp
        

    def decode(self, shortUrl):
        if shortUrl in self.tiny2url:
            return self.tiny2url[shortUrl]
        else:
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
