import heapq

# Possible moves: up, down, left, right
MOVES = [(-1,0), (1,0), (0,-1), (0,1)]


def print_state(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()


def heuristic(state, goal):
    # Misplaced tiles heuristic (ignore blank = 0)
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                if state[i][j] != goal[i][j]:
                    count += 1
    return count


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    x, y = find_blank(state)
    neighbors = []

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


def a_star(start, goal):
    start = tuple(tuple(row) for row in start)
    goal = tuple(tuple(row) for row in goal)

    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), 0, start))
    closed = set()

    parent = {start: None}

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()

            print("Solution path:\n")
            for step in path:
                print_state(step)

            print("Total moves:", len(path) - 1)
            return

        closed.add(current)

        for neighbor in get_neighbors(current):
            if neighbor in closed:
                continue

            if neighbor not in parent:
                parent[neighbor] = current
                g_new = g + 1
                f_new = g_new + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_new, g_new, neighbor))

    print("No solution found")


initial_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

goal_state = [
    [2, 8, 1],
    [0, 4, 3],
    [7, 6, 5]
]

a_star(initial_state, goal_state)

