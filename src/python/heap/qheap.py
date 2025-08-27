from minheap import MinHeap

heap = MinHeap()
heap.insert(4)
heap.insert(9)

print(heap.peek())
heap.delete(4)
print(heap.peek())

