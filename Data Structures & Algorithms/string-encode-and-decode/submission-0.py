class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output += (str(len(i)) + "#" + i)
        return output
            
    def decode(self, s: str) -> List[str]:
        i = 0
        integer = ""
        output = []
        while (i < len(s)):
            if (s[i] == "#"):
                i += 1
                output.append(s[i:i+int(integer)])
                i += int(integer)
                integer = ""
            else:
                integer += s[i]
                i += 1
        return output