from collections import deque

def quickestWayUp(ladders, snakes):
    # Create board mapping: square → new position after ladder/snake
    board = {i: i for i in range(1, 101)}
    
    for start, end in ladders:
        board[start] = end
    for start, end in snakes:
        board[start] = end

    # BFS setup
    visited = [False] * 101  # index 0 unused
    queue = deque()
    queue.append((1, 0))  # (current square, number of rolls)
    visited[1] = True

    while queue:
        square, rolls = queue.popleft()

        # Reached the goal
        if square == 100:
            return rolls

        # Try all dice rolls from 1 to 6
        for i in range(1, 7):
            next_square = square + i
            if next_square <= 100:
                dest = board[next_square]
                if not visited[dest]:
                    visited[dest] = True
                    queue.append((dest, rolls + 1))

    # If 100 is not reachable
    return -1
