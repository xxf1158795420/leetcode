class Solution(object):
    pre=0
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        
        
        if root.right:
            self.bstToGst(root.right)
        self.pre=self.pre+root.val
        root.val=self.pre
        if root.left:
            self.bstToGst(root.left)
        return root
        """
        st=[]
        node=root
        while st or node:
            while node:
                st.append(node)
                node=node.right
            node=st.pop()
            self.pre=self.pre+node.val
            node.val=self.pre
            node=node.left
        return root
