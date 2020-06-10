class Node: 
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
      
def findLCA(root, n1, n2, parent): 
    if root is None: 
        return None
  
    # If either n1 or n2 matches with root's key, report 
    #  the presence by returning root (Note that if a key is 
    #  ancestor of other, then the ancestor key becomes LCA 
    if root.key == n1 or root.key == n2: 
        return root , parent  
  
    # Look for keys in left and right subtrees 
    left_lca = findLCA(root.left, n1, n2, root)  
    right_lca = findLCA(root.right, n1, n2, root) 
  
    # If both of the above calls return Non-NULL, then one key 
    # is present in once subtree and other is present in other, 
    # So this node is the LCA 
    if left_lca and right_lca: 
        return root , parent 
  
    # Otherwise check if left subtree or right subtree is LCA 
    return left_lca if left_lca is not None else right_lca 
  
  
# Driver program to test above function 
  
# Let us create a binary tree given in the above example 

def LCA(root,n1,n2):
    parent = None
    node,parent = findLCA(root,n1,n2,parent)
    if node.key in (n1,n2):
        node = None
    if parent is None:
        return node.key
    elif node is None:
        return parent.key
    else:
        return parent.key,node.key

root = Node(2) 
root.left = Node(1) 
root.right = Node(3) 
root.right.left = Node(4) 
root.right.right = Node(5) 
root.right.right.right = Node(6)
print("LCA(1,5) = ", LCA(root, 1, 5))
print("LCA(3,6) = ", LCA(root, 3, 6)) 
print("LCA(4,6) = ", LCA(root, 4, 6)) 

