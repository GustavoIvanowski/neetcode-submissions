class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for i in strs:
            count = [0]*26
            for j in i:
                count[ord(j) - ord('a')] += 1
            count = tuple(count)
            if count in anagramMap:
                anagramMap[count].append(i)
            else:
                anagramMap[count] = [i]
        return list(anagramMap.values())