# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    array = []
    numberOfVisited = 0
    count = 0
    helperTraveseReverseInOrder(tree, array, count,k)
    print("the list is  = ", array)
    print(" k = ", k)
    return array[k-1]
    

def helperTraveseReverseInOrder(tree, array, count, k):

    if tree is not None and count < k:
        helperTraveseReverseInOrder(tree.right, array, count, k)
        array.append(tree.value)
        count += 1
        helperTraveseReverseInOrder(tree.left, array, count, k)
        
        

    