class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            length = len(s)
            ret += str(length) + "#" + s
        

        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            len_to_read = ""
            while s[i].isnumeric() and s[i] != "#" and i < len(s):
                len_to_read += s[i]
                i += 1
            
            # s[i] is now #
            i += 1

            # s[i] now points to first char of string of length len_to_read
            len_to_read = int(len_to_read)
            ret.append(s[i: i + len_to_read])
            i = i + len_to_read

        return ret

