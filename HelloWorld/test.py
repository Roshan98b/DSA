class A:
    def __init__(self, arr):
        self.arr1 = [list(x) for x in arr]
        self.arr2 = [list(x) for x in arr]
        self.arr2[1][0] = 2

arr = [[6],[5],[4],[3],[2],[1]]
a = A(arr)

print (a.arr1)
print (a.arr2)

