from collections import deque

def display_maze(maze):
    for row in maze:
        print(''.join(row))
    print()

def find_positions(maze, start_symbol='S', goal_symbol='G'):
    start, goal = None, None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == start_symbol:
                start = (i, j)
            elif cell == goal_symbol:
                goal = (i, j)
    if not start or not goal:
        raise ValueError("Maze must contain 'S' (start) and 'G' (goal) symbols.")
    return start, goal

# Depth-First Search
def dfs(maze, start, goal):
    stack = [start]
    visited = set()
    parent = {}

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            break

        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = current[0] + d[0], current[1] + d[1]
            if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and maze[ni][nj] not in ('#', 'S') and (ni, nj) not in visited:
                stack.append((ni, nj))
                parent[(ni, nj)] = current

    current = goal
    while current != start:
        if current != goal:  # Ensure the goal cell remains 'G'
            maze[current[0]][current[1]] = '*'
        current = parent.get(current, start)
    maze[start[0]][start[1]] = 'S'
    return maze

# Example maze
maze = [
    list("################"),
    list("#******#########"),
    list("#*####*********#"),
    list("# ############*#"),
    list("#*****#*#***##G#"),
    list("#*###*###*#****#"),
    list("#S###*****######"),
    list("################"),
]

start, goal = find_positions(maze)

print("Original Maze:")
display_maze(maze)

# Solve using DFS
dfs_solution = [row[:] for row in maze]
dfs_solution = dfs(dfs_solution, start, goal)
print("Maze Solved with DFS:")
display_maze(dfs_solution)
