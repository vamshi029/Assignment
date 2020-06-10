from collections import deque
class Node: 
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
        


def bfs(root):
    if not root:
        return 
    queue = deque([])
    queue.append(root)
    while(queue):
        node = queue.popleft()
        print(node.key,end=' ')
        if node.left :
            queue.append(node.left)
        if node.right : 
            queue.append(node.right)

root = Node(1) 
root.right = Node(2) 
root.right.right = Node(5) 
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)
bfs(root)
