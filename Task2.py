from collections import deque
import heapq

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

# A* Algorithm

def a_star_with_path_costs(maze, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    g_score = {start: 0}
    parent = {}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            break

        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = current[0] + d[0], current[1] + d[1]
            if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and maze[ni][nj] not in ('#', 'S'):
                tentative_g_score = g_score[current] + 1
                if (ni, nj) not in g_score or tentative_g_score < g_score[(ni, nj)]:
                    g_score[(ni, nj)] = tentative_g_score
                    f_score = tentative_g_score + abs(ni - goal[0]) + abs(nj - goal[1])
                    heapq.heappush(open_set, (f_score, (ni, nj)))
                    parent[(ni, nj)] = current

    # Reconstruct the path and assign costs
    current = goal
    while current != start:
        if current != goal:  # Ensure the goal cell remains 'G'
            maze[current[0]][current[1]] = str(g_score[current])[-1]  # Show path cost as last digit
        current = parent.get(current, start)
    maze[start[0]][start[1]] = 'S'
    return maze

# Example maze
maze = [
    list("###############"),
    list("#S#     #    #"),
    list("# # ### # #  #"),
    list("# #   # # # G#"),
    list("# ### # ###  #"),
    list("#     #      #"),
    list("###############"),
]

start, goal = find_positions(maze)

print("Original Maze:")
display_maze(maze)

# Solve using A*
a_star_solution = [row[:] for row in maze]
a_star_solution = a_star_with_path_costs(a_star_solution, start, goal)
print("Maze Solved with A* Path Costs:")
display_maze(a_star_solution)
