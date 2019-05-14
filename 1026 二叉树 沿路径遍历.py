class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        res=[]
        if not root:return 0
        def dfs(node,tmp):
            if not node.left and not node.right:
                res.append(tmp+[node.val])
            if node.left:
                dfs(node.left,tmp+[node.val])
            if node.right:
                dfs(node.right,tmp+[node.val])
        dfs(root,[])
        ans=[max(x)-min(x) for x in res]
        return max(ans)
        """
        st=[[root,root.val,root.val]]
        mx=0
        while st:
            l=len(st)
            for _ in range(l):
                node,cur_mx,cur_mn=st.pop()
                if node.val<cur_mn:
                    cur_mn=node.val
                if node.val>cur_mx:
                    cur_mx=node.val
                mx=max(mx,cur_mx-cur_mn)
                if node.left:st.append([node.left,cur_mx,cur_mn])
                if node.right:st.append([node.right,cur_mx,cur_mn])
        return mx
