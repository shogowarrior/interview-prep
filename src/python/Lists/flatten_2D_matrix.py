# Design an iterator to flatten a 2D vector. It should support next and hasNext operations.



class MatrixIterator:

    def __init__(self, matrix):
        """
        Initialize the iterator with a 2D matrix.
        
        :param matrix: List of lists representing the 2D matrix
        """
        self.matrix = matrix
        self.row = 0
        self.col = 0
        self.total_rows = len(matrix)
        self.total_cols = len(matrix[0]) if self.total_rows > 0 else 0
        

    def hasNext(self) -> bool:
        return self.row < self.total_rows and self.col < self.total_cols
    
    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration("No more elements in the matrix")
        
        value = self.matrix[self.row][self.col]
        self.col += 1
        
        if self.col == self.total_cols:
            self.col = 0
            self.row += 1
            
        return value


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

iterator = MatrixIterator(matrix)
while iterator.hasNext():
    print(iterator.next())  