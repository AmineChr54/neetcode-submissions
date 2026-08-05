# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        self.pre_ind = 0

        def array_to_tree(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_ind]
            self.pre_ind +=1

            root = TreeNode(val = root_val)

            mid = inorder_map[root_val]
            root.left = array_to_tree(left, mid-1)
            root.right = array_to_tree(mid+1, right)
            
            return root

        return array_to_tree(0, len(preorder) -1)