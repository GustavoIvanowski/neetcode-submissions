class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        valSearch = defaultdict(int)
        out = 0
        for num in nums:
            if valSearch[num] != 0: continue
            length = valSearch[num - 1] + valSearch[num + 1] + 1
            if length > out: out = length
            valSearch[num] = length
            valSearch[num - valSearch[num - 1]] = length
            valSearch[num + valSearch[num + 1]] = length
        return out
        


# [9, 8, 7, 6, 1, 2, 3, 4, 5]
# {9: 9, 8: 2, 7: 3, 6: 4, 1: 9, 2: 2, 3: 3, 4: 4, 5: 9}
# length = valSearch[i - 1] + valSearch[i + 1] + 1
# valSearch[i - valSearch[i - 1]] = length
# valSearch[i - valSearch i + 1] = length