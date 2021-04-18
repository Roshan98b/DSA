class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None 

    def insert(self, root, data):
        if (root == None):
            root = Node(data)
            if (self.root == None):
                self.root = root
            return
        if(data <= root.data):
            if(root.left == None):
                root.left = Node(data)
                return
            else:
                self.insert(root.left, data)
        else:
            if(root.right == None):
                root.right = Node(data)
                return
            else:
                self.insert(root.right, data)

    def get_node_count(self, root):
        if (root == None):
            return 0
        else:
            return self.get_node_count(root.left) + self.get_node_count(root.right) + 1

    def is_in_tree(self, root, data):
        if (root == None):
            return False
        elif (data == root.data):
            return True
        elif (data < root.data):
            return self.is_in_tree(root.left, data)
        elif (data > root.data):
            return self.is_in_tree(root.right, data)

    def get_successor(self, root, data):
        if (root == None):
            return None
        elif (data == root.data):
            if (root.right == None):
                return None
            return root.right.data
        elif (data < root.data):
            return self.get_successor(root.left, data)
        elif (data > root.data):
            return self.get_successor(root.right, data)

    def get_height(self, root):
        if (root == None):
            return 0
        else:
            return 1 + max(self.get_height(root.left), self.get_height(root.right))


    def get_min(self, root):
        if (root == None):
            return None
        elif (root.left == None):
            return root.data
        else:
            return self.get_min(root.left)

    def get_max(self, root):
        if (root == None):
            return None
        elif (root.right == None):
            return root.data
        else:
            return self.get_max(root.right)

    def delete_value(self, root, data, prev = None):
        if (root == None):
            return False
        elif (data < root.data):
            return self.delete_value(root.left, data, root)
        elif (data > root.data):
            return self.delete_value(root.right, data, root)
        else:
            if (root.left == root.right == None):
                if (root.data <= prev.data):
                    prev.left = None
                else:
                    prev.right = None
                del root
                return True
            elif (root.right == None):
                if (root.data <= prev.data):
                    prev.left = root.left
                else:
                    prev.right = root.right
                del root
                return True                
            elif (root.left == None):
                if (root.data <= prev.data):
                    prev.left = root.right
                else:
                    prev.right = root.right
                del root
                return True
            else:
                temp = root.right
                prevtemp = None
                while (temp.left != None):
                    prevtemp = temp
                    temp = temp.left
                root.data = temp.data
                if (temp.left == temp.right == None):
                    prevtemp.left = None
                    del temp
                else:
                    prevtemp.left = temp.right
                    del temp
                return True 

    def delete_tree(self, root):
        if (root == None):
            return
        else: 
            delete_tree(root.left)
            delete_tree(root.right)
            del (root)


def inorder(current):
    if (current == None):
        return
    else:
        inorder(current.left)
        print (current.data)
        inorder(current.right)

def preorder(current):
    if (current == None):
        return
    else:
        print (current.data)
        preorder(current.left)
        preorder(current.right)    

def postorder(current):
    if (current == None):
        return
    else:
        postorder(current.left)
        postorder(current.right)
        print (current.data)


# Main function
if __name__ == "__main__":
    bst = Tree()
    
    bst.insert(bst.root, 10)
    bst.insert(bst.root, 5)
    bst.insert(bst.root, 11)
    bst.insert(bst.root, 233)
    bst.insert(bst.root, -4)
    bst.insert(bst.root, 11)
    bst.insert(bst.root, 123)
    bst.insert(bst.root, 77)
    bst.insert(bst.root, 300)
    bst.insert(bst.root, 1)

    print ("Inorder")
    inorder(bst.root)
    print ("Preorder")
    preorder(bst.root)
    print ("Postorder")
    postorder(bst.root)

    print ("Node count: ", bst.get_node_count(bst.root))
    print("Height: ", bst.get_height(bst.root))


    print ("5 is in tree?:", bst.is_in_tree(bst.root, 5))
    print ("2 is in tree?:", bst.is_in_tree(bst.root, 2))

    print ("Successor of 5?:", bst.get_successor(bst.root, 5))
    print ("Successor of 11?:", bst.get_successor(bst.root, 2))
    print ("Successor of 1?:", bst.get_successor(bst.root, 1))

    print ("Min: ", bst.get_min(bst.root))
    print ("Max: ", bst.get_max(bst.root))
    
    bst.delete_value(bst.root, 11)
    bst.delete_value(bst.root, 77)
    bst.delete_value(bst.root, 10)
    
    print ("Inorder")
    inorder(bst.root)
    print ("Preorder")
    preorder(bst.root)

