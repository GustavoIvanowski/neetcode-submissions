class Solution:
    def countOdds(self, low: int, high: int) -> int:
        tween = (high - low) // 2
        if not (low % 2 or high % 2):
            return tween
        return tween + 1


    # cases: 
    #   [odd, odd]
    #   [3, 9]
    #   tween + 1
    #   [even, odd]
    #   [2, 9]
    #   tween + 1
    #   [even, even]
    #   [2, 10]
    #   tween
    #   [odd, even]
    #   [3, 10]
    #   tween + 1