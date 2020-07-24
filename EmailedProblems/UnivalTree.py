# Problem Description:
# 
# A unival tree (which stands for "universal value") is a tree where all 
# nodes under it have the same value.
# 
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTestTree1():
    left1Leaf1 = Node(1)
    left1Leaf2 = Node(1)
    right1Leaf = Node(1)

    right0Leaf = Node(0)

    lowestSubTree = Node(1, left1Leaf2, right1Leaf)
    middleSubTree = Node(0, lowestSubTree, right0Leaf)
    root = Node(0, left1Leaf1, middleSubTree)
    return root


def getNumUniValSubTrees(binaryTree):
    if binaryTree.left == None and binaryTree.right == None:
        return 1
    
    elif not binaryTree.left == None and binaryTree.right == None:
        leftSubTreeNumUniVal = getNumUniValSubTrees(binaryTree.left)
        if binaryTree.left.val == binaryTree.val:
            leftSubTreeNumUniVal += 1
        return leftSubTreeNumUniVal

    elif binaryTree.left == None and not binaryTree.right == None:
        rightSubTreeNumUniVal = getNumUniValSubTrees(binaryTree.right)
        if binaryTree.right.val == binaryTree.val:
            rightSubTreeNumUniVal += 1
        return rightSubTreeNumUniVal

    else:
        total = getNumUniValSubTrees(binaryTree.right)
        total += getNumUniValSubTrees(binaryTree.left)
        if binaryTree.right.val == binaryTree.val and binaryTree.left.val == binaryTree.val:
            total += 1
        return total
            
        
def main():
    testTree = buildTestTree1()

    print("Testing tree with following structure:")
    print("   0")
    print("  / \\")
    print(" 1   0")
    print("    / \\")
    print("   1   0")
    print("  / \\")
    print(" 1   1")
    print("Expected Result - 5")

    print(getNumUniValSubTrees(testTree))


main()




