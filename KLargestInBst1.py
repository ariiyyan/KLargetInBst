# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    array = []
    
    helperTraveseInOrder(tree, array, k)
    print("list is = , ", array)
    return array[len(array)- k]
    

def helperTraveseInOrder(tree, array, k):

    if tree is not None:
        
        helperTraveseInOrder(tree.left, array, k)
        array.append(tree.value)
        helperTraveseInOrder(tree.right, array, k)

    