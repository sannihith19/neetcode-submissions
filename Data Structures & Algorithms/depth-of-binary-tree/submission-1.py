class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        leftdepth = 1 + self.maxDepth(root.left) 
        rightdepth = 1 + self.maxDepth(root.right)

        return max(leftdepth, rightdepth) 