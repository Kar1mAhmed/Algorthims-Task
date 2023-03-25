class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    def in_order_recursive(self,root):
        ans = []
        if not root:
            in_order_re



root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

root.left = node2
root.right = node3


node4= TreeNode(4)
node5= TreeNode(5)
node6= TreeNode(6)
node7= TreeNode(7)


node2.left = node4

node3.left = node5
node3.right= node6

node6.right = node7

# that's how the tree look, it should have a depth of 4
#                1
#             2     3
#          4      5    6
#                         7

#lets build a function that can find the depth

def dfs(root, depth):
            if not root : 
                return depth
            print(root.val)
            return max(dfs(root.right, depth+ 1) , dfs(root.left, depth + 1)) 

print(dfs(root,0))