class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        counts = defaultdict(int)
        for i in range(len(arr)):
            counts[arr[i]] += 1

        count = 0
        for i in range(len(arr)):
            if counts[arr[i]] == 1:
                count += 1
                if count == k:
                    return arr[i]
        return ""
                
            
