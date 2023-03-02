'''binary tree:
a node can have maximum only two chidren'''

'''#implementation of binary tree
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
node1=BinaryTreeNode(50)
node2=BinaryTreeNode(20)
node3=BinaryTreeNode(45)
node4=BinaryTreeNode(11)
node5=BinaryTreeNode(15)
node6=BinaryTreeNode(30)
node7=BinaryTreeNode(78)
node1.leftChild=node2
node1.rightChild=node3
node2.leftChild=node4
node2.rightChild=node5
node3.leftChild=node6
node3.rightChild=node7
print("root node is:")
print(node1.data)
print("left child of the node is:")
print(node1.leftChild.data)
print("right child of the node is:")
print(node1.rightChild.data)
print("node is:")
print(node2.data)
print("left child of the node is:")
print(node2.leftChild.data)
print("right child of the node is:")
print(node2.rightChild.data)
print("node is:")
print(node3.data)
print("left child of the node is:")
print(node3.leftChild.data)
print("right child of the node is:")
print(node3.rightChild.data)'''

'''binary tree traversal:
1.inorder:left-root-right_LDR
2.preorder:root-left-right_DLR
3.postorder:left-right-root_LRD'''

'''there are two types of traversal.they are:
1.bfs(breadth first search)
2.dfs(depth first search)'''

'''class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key        
def printInorder(root):
    if root:
        #first recur on left child
        printInorder(root.left)
        #then print the data of node
        print(root.val,end=" ")
        #now recur on right child
        printInorder(root.right)
def printPostorder(root):
    if root:
        #first recur on left child
        printPostorder(root.left)
        #then recur on right child
        printPostorder(root.right)
        #now print the data of node
        print(root.val,end=" ")
def printPreorder(root):
    if root:
        #first print the data of node
        print(root.val,end=" ")
        #then recur on left child
        printPreorder(root.left)
        #finally recur the right child
        printPreorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("pre-order:")
printPreorder(root)
print("\nin-order:")
printInorder(root)
print("\npost-order:")
printPostorder(root)'''

'''full binary tree:
all the nodes will have 0 or 2 children'''

'''complete binary tree
1.every level should be full or complete
2.in last level if it is incomplete nodes should present at extreme left side'''

'''perfect binary tree:
1.all internal nodes which has 2 children and both the leaf nodes should be at
same level'''

'''balanced binary tree:
for all the nodes,height of left sub tree-height of right subtree can be 0 or 1'''

'''binary search tree:
1.all the left side elements should be lesser than its parent
2.all the right side elements should be greater than its parent'''

'''#bst-insert
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
#a new node with the given key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
#inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
r=Node(50)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,60)
r=insert(r,80)
inorder(r)'''

'''class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
#found in that tree.note that the entire tree does not need to be searched
def minValueNode(node): #right sub tree
    current=node
    #loop down to find the leftmost leaf
    while(current.left is not None):
        current=current.left
    return current
#given a binary search tree and a key
def deleteNode(root,key):
    #base case
    if root is None:
        return root
    #key<root,it lies in left subtree
    if key<root.key:
        root.left=deleteNode(root.left,key)
    elif(key>root.key):
        root.right=deleteNode(root.right,key)
    #if key is same as root's key,then this is to be deleted
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        #node with two children:
        #get the inorder accessor
        temp=minValueNode(root.right)
        root.key=temp.key
        root.right=deleteNode(root.right,temp.key)
    return root
root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)
print("inorder traversal of the given tree:")
inorder(root)
print("\nDelete 20")
root=deleteNode(root,20)
print("inorder traversal of modified tree:")
inorder(root)
print("\nDelete 30")
root=deleteNode(root,30)
print("inorder traversal of modified tree:")
inorder(root)
print("\nDelete 50")
root=deleteNode(root,50)
print("inorder traversal of modified tree:")           
inorder(root)'''    
        


              
        
        
            





