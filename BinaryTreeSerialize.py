# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


def serialize(node):
    serializedData = []
    if node:
        serializedData.append(node.val)
        serializedData.append(serialize(node.left))
        serializedData.append(serialize(node.right))

    return serializedData

def deserialize(stringdata):
    numElements = len(stringdata)
    if numElements == 0:
        return None
    elif numElements == 1:
        return Node(stringdata[0])
    else:
        return Node(stringdata[0], deserialize(stringdata[1]), deserialize(stringdata[2]))

def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    res = deserialize(serialize(node)).left.left.val
    assert res == 'left.left', "Incorrect"
    print(res)
main()