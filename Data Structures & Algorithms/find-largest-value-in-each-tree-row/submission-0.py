# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        output = []

        thisLevel = []
        nextLevel = []
        nextLevel.append(root)
        
        while len(nextLevel) != 0 or len(thisLevel) != 0:
            # check max of next level
            if len(thisLevel) == 0:
                maxVal = float('-inf')
                for i in nextLevel:
                    maxVal = max(maxVal, i.val)
                print(maxVal)
                output.append(maxVal)
                thisLevel = nextLevel.copy()
                nextLevel = []
            
            curr = thisLevel.pop(0)
            if curr.left:
                nextLevel.append(curr.left)
            if curr.right:
                nextLevel.append(curr.right)
        
        return output

# thisLevel = []
# nextLevel = [1, 7, 3]
# output = [5, 9]
            
