class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        distinctStrings = set()
        notDistinctStrings = set()
        for i in range(len(arr)):
            if arr[i] in distinctStrings:
                distinctStrings.remove(arr[i])
                notDistinctStrings.add(arr[i])
            elif arr[i] not in notDistinctStrings:
                distinctStrings.add(arr[i])

        count = 0
        for i in range(len(arr)):
            if arr[i] in distinctStrings:
                count += 1
                if count == k:
                    return arr[i]
        return ""
                
            
