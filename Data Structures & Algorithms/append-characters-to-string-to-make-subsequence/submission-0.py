class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if (len(t) == 0): return 0
        if (len(s) == 0): return len(t)
        i = 0 # s pointer
        j = 0 # t pointer
        while i < len(s):
            if s[i] == t[j]:
                j += 1
                if j == len(t):
                    return 0
            i += 1
        return len(t) - j