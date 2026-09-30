class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        counts = [[] for i in range(len(nums) + 1)]
        for i in nums:
            freqMap[i] = 1 + freqMap.get(i, 0)
        for key, v in freqMap.items():
            counts[v].append(key)
        
        output = []
        for i in range(len(nums), 0, -1):
            for n in counts[i]:
                output.append(n)
                if len(output) == k:
                    return output

