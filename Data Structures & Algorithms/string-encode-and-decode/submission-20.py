class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = ""
        for word in strs:
            ret += str(int(len(word)))
            ret += ","
        ret += "#"

        for word in strs:
            ret += word
        
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        lengths = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == '#':
                break
            if c == ',':
                i += 1
                continue
            if c.isnumeric():
                length_str = ""
                while s[i].isnumeric():
                    length_str += s[i]
                    i += 1
                lengths.append(int(length_str))
        
        ret = []
        i += 1
        for length in lengths:
            ret.append(s[i: i + length])
            i += length
        
        return ret
        

        


        

