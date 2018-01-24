class Node:
    def __init__(self, value, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild

def searchSum(tree, reqSum):
    node = tree
    validPaths = []
    currentPath = [node]
    visited = [node]
    while len(currentPath) > 0:
        if node.lchild and (node.lchild not in visited):
            currentPath.append(node.lchild)
            visited.append(node.lchild)
            node = node.lchild
        elif node.rchild and (node.rchild not in visited):
            currentPath.append(node.rchild)
            visited.append(node.rchild)
            node = node.rchild
        else:
            pathValues = [i.value for i in currentPath]
            if sum(pathValues) == reqSum:
                validPaths.append(pathValues)
            currentPath.pop()
            if len(currentPath) > 0:
                node = currentPath[-1]
    return validPaths

# # example Tree
# testTree = Node(5, Node(4, Node(11, Node(7), Node(2))), Node(8, Node(13), Node(4, Node(5), Node(1))))

# # example test case
# print(searchSum(testTree, 22))
