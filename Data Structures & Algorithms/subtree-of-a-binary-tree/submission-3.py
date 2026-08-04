# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if (not p) ^ (not q):
                return False
            elif not p and not q:
                return True

            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right) and p.val == q.val

        if not subRoot:
            return True

        if not root:
            return subRoot is None

        if root.val == subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or isSameTree(root, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
