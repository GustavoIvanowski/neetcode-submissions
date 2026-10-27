# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        switch = True; # true, false : start from left, start from right

        queue1 = []
        queue2 = []
        curr = root

        level = []
        output = []

        while queue2 or queue1 or curr:
            if curr: # if curr is a node, not None
                if switch:
                    queue2.append(curr.left)
                    queue2.append(curr.right)
                else:
                    queue2.append(curr.right)
                    queue2.append(curr.left)

                level.append(curr.val)
                
            if not queue1: # once level cleared, add level to output and level up
                queue1 = queue2.copy()
                queue2 = []
                output.append(level)
                level = []
                switch = not switch

            
            curr = queue1.pop(-1)

        return output


#       3
#     /    \
#    9     20
#         /  \
#       15    7
# 
# 
# 

            