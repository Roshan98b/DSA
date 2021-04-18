class Node:

    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def inorder(current):
    inorder_list = []
    stack = [current]
    while (stack != [None]):
        current = stack[len(stack)-1]
        if (current == None):
            stack.pop()
            child = stack.pop()
            inorder_list.append(child.data)
            stack.append(child.right)
        else:
            stack.append(current.left)
    return inorder_list

def preorder(current):
    preorder_list = []
    stack = [current]
    while (stack != [None]):
        current = stack[len(stack)-1]
        if (current == None):
            stack.pop()
            child = stack.pop()
            stack.append(child.right)
        else:
            stack.append(current.left)
            preorder_list.append(current.data)
    return preorder_list

