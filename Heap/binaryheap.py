class BHeap:

    def __init__(self, data=[]):
        self.heap = data
        self.index = {}

    def __swin(self, pos):
        parent = int(((pos - 2)/2) if (pos % 2) else (pos/2))
        while (pos > 0 and self.heap[parent] >= self.heap[pos]):
            self.__swap(pos, parent)
            pos = parent
            parent = int(((pos - 2)/2) if (pos % 2) else (pos/2))

    def __sink(self, pos):
        child1 = 2*pos + 1
        child2 = 2*pos + 2 
        while (child1 < len(self.heap) or child2 < len(self.heap)):
            if (child1 < len(self.heap) and child2 < len(self.heap)):
                if self.heap[pos] < self.heap[child1] and self.heap[pos] < self.heap[child2]:
                    break
                child = child1 if self.heap[child1] < self.heap[child2] else child2
            elif child1 < len(self.heap):
                if self.heap[pos] < self.heap[child1]:
                    break
                child = child1
            else:
                if self.heap[pos] < self.heap[child2]:
                    break
                child = child2
            self.__swap(pos, child)
            pos = child
            child1 = 2*pos + 1
            child2 = 2*pos + 2

    def __swap(self, a, b):
        self.index[self.heap[a]] = b
        self.index[self.heap[b]] = a
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp

    def insert(self, data):
        self.heap.append(data)
        self.index[data] = len(self.heap)-1
        self.__swin(len(self.heap)-1)

    def poll(self):
        if (len(self.heap)):
            self.__swap(0, len(self.heap)-1)
            pop = self.heap.pop()
            self.index.pop(pop)
            self.__sink(0)
            return pop
        else:
            return None
    
    def remove(self, data):
        if (data in self.index):
            pos = self.index[data]
            self.__swap(pos, len(self.heap)-1)
            pop = self.heap.pop()
            self.index.pop(pop)
            self.__sink(pos)
            self.__swin(pos)
            return pop
        else:
            return None

    def display(self):
        print (self.heap, self.index)

if __name__ == "__main__":

    heap = BHeap()
    heap.insert(6)
    heap.insert(4)
    heap.insert(7)
    heap.insert(8)
    heap.insert(1)
    heap.display()
    heap.poll()
    heap.poll()
    heap.display()
    heap.insert(9)
    heap.insert(10)
    heap.insert(11)
    heap.insert(12)
    heap.insert(13)
    heap.insert(14)
    heap.display()
    print (heap.remove(7))
    heap.display()
