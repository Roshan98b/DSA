import sys
sys.path.insert(1, '/mnt/c/Users/robadrin/source/repos/DSA')

from Trees.bt import Node, inorder

if __name__ == '__main__':
     
    N = 7
    root = Node(50)
    root.left = Node(30)
    root.right = Node(60)
    root.left.left = Node(20)
    root.left.right = Node(25)
    root.right.left = Node(10)
    root.right.right = Node(40)

    inordered_list = inorder(root)
    print ("Inoder:")
    print (inordered_list)

    cnt, j = 0, 1
    for ele in inordered_list:
        for i in range(j, N):
            if (ele > inordered_list[i]):
                cnt += 1
                print ("(", ele, ",", inordered_list[i], ")")
        j += 1 
    
    print ("Count: ", cnt)
