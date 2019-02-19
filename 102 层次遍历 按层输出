class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=[root]
        res=[]
        while queue:
            templist=[]
            templen=len(queue)
            for i in range(templen):
                temptree=queue.pop(0)
                templist.append(temptree.val)
                if temptree.left:
                    queue.append(temptree.left)
                if temptree.right:
                    queue.append(temptree.right)
            res.append(templist)
        return res
