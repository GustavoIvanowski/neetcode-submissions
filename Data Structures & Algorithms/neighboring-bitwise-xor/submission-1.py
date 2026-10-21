class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        if len(derived) == 1:
            return not bool(derived[0])
        first = False
        curr = -1
        if derived[0]:
            curr = True
        else:
            curr = False
        for i in range(1, len(derived) - 1):
            if derived[i]:
                curr = not curr
        if derived[-1]:
            return curr != first
        else:
            return curr == first

            
# [0, 1, 0, 1]
# [0, 0, 1, 1
# first = 0
# curr = 1