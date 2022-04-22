def preoder(subtree):
    if subtree:
        print(subtree.data)
        preoder(subtree.left)
        preoder(subtree.rigth)

def inorder(subtree):
    if subtree:
        inorder(subtree.left)
        print(subtree.data)
        inorder(subtree.rigth)
        
def postorder(subtree):
    if subtree:
        postorder(subtree.left)
        postorder(subtree.rigth)
        print(subtree.data)