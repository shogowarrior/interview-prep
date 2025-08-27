class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i): return (i - 1) // 2
    def _left(self, i): return 2 * i + 1
    def _right(self, i): return 2 * i + 2

    def build_heap(self, array):
        # Initialize the heap with the provided array
        self.heap = array
        n = len(self.heap)

        # Start from the last non-leaf node and heapify down
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)

    def peek(self):
        return self.heap[0] if self.heap else None

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, val):
        try:
            # Find the index of the element to delete
            index = self.heap.index(val)
            last_index = len(self.heap) - 1

            # Swap the element with the last element
            self.heap[index], self.heap[last_index] = self.heap[last_index], self.heap[index]

            # Remove the last element (the element to be deleted)
            self.heap.pop()

            # Restore heap property by heapifying up or down
            if index < len(self.heap):
                self._heapify_up(index)
                self._heapify_down(index)
        except ValueError:
            print(f"Value {val} not found in heap.")
    
    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last to root
        self._heapify_down(0)
        return min_val

    def _heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self._parent(i)]:
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)

    def _heapify_down(self, i):
        size = len(self.heap)
        smallest = i

        left = self._left(i)
        right = self._right(i)

        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

    def __str__(self):
        return str(self.heap)