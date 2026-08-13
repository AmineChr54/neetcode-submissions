# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            
            # Current node value must strictly fit within (low, high)
            if not (low < node.val < high):
                return False
            
            # Left subtree values must be < node.val
            # Right subtree values must be > node.val
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))

        return validate(root)"""
        result = []
        def inorderDFS(root):
            if not root:
                return
            inorderDFS(root.left)
            result.append(root.val)
            inorderDFS(root.right)

        inorderDFS(root)
        print(result)
        for i in range(1, len(result)):
            if result[i] <= result[i-1]:
                return False
        return True
