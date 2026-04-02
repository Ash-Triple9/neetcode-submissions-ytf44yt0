class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr = ""
        delim = '#'
        for word in strs:
            size = len(word)
            encodedstr += str(size)+delim+word
        return encodedstr

    def decode(self, s: str) -> List[str]:
        decodedstr = []
        i = 0
        while i < len(s):
            num = ''
            while s[i]!= "#":
                num+=s[i]
                i+=1
            i+=1
            num = int(num)
            decodedstr.append(s[i:i+num])
            i+=num
        return decodedstr


