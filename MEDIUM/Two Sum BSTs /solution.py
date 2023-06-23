class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        if not root1 or not root2:
            return False
        
        def get_all_nodes(node):
            
            stack = [node]
            nodes = set()
        
            while stack:
                current_node = stack.pop()
                
                nodes.add(current_node.val)
                if current_node.left:
                    stack.append(current_node.left)
                if current_node.right:
                    stack.append(current_node.right)
                    
            return nodes
        
        
        nodes1 = get_all_nodes(root1)
        
        stack = [root2]
        while stack:
            current_node = stack.pop()
            node_target = target - current_node.val
            if node_target in nodes1:
                return True
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
                
        return False
