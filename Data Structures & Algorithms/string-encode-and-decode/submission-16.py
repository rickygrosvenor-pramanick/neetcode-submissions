class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ','
        res += '#'
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        sizes = []
        i = 0
        while i < len(s) and s[i] != '#':
            if s[i] == ',':
                i += 1
                continue
            length = ""
            while s[i].isnumeric():
                length += s[i]
                i += 1
            sizes.append(int(length))
        
        # now i is the index of #
        i += 1
        # now i is the first char of the first word
        ret = []
        for size in sizes:
            ret.append(s[i: i + size])
            i = i + size
        
        return ret

        


        

