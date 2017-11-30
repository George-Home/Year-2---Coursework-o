class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
  
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)

def del_Node(tree, remove):
    trees = tree.value
    parent = BinTreeNode(remove)

    while tree and tree.value != remove:                #finds node to be removed
        parent = tree.value
        if remove < tree.value:
            tree.value = tree.left
        elif remove > tree.value:
            tree.value = tree.right

    
    if tree.left is None and tree.right is None:        #no children
            if remove < parent.value:
                parent.left = None
            else:
                parent.right = None

    elif tree.left and tree.right is None:              #only left child
        if remove < parent.value:
            parent.left = tree.left
        else:
            parent.right = tree.left

    elif tree.right and tree.left is None:          #only right child
        if remove < parent.value:
            parent.left = tree.right
        else:
            parent.right = tree.right

    else:                                           #both children
        remParent = tree.value
        remNode = tree.right

        while remNode.left:             #finds lowest value for right side of tree
            remParent = remNode
            remNode = remNode.left

        tree.value = remNode.value

        if tree.right:
            if parent.value > tree.value:
                parent.left = tree.right
            elif parent.value < tree.value:
                parent.right = tree.right

        else:
            if tree.value < parent.value:
                parent.left = None
            else:
                parent.right = None

    return tree
    print(tree.value)
 
if __name__ == '__main__':
   

  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
  print("")
  del_Node(t,6)
  in_order(t)
