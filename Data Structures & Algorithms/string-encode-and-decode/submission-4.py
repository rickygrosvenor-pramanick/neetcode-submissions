class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ''
        for s in strs:
            length = len(s)
            ret += str(length)
            ret += '#'
            ret += s
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        num_set = {str(x) for x in range(0, 10)}

        i = 0
        while i < len(s):
            length = ''
            while s[i] in num_set:
                length += s[i]
                i += 1
            length = int(length)
            i += 1
            ret.append(s[i: i + length])
            i = i + length
        return ret
        

