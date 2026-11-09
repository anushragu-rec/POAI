import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_heap = [(heuristic(start, goal), 0, start)]
    came_from = {}
    cost_so_far = {start: 0}
    closed = set()

    while open_heap:
        _, cost, current = heapq.heappop(open_heap)
        if current in closed:
            continue
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        closed.add(current)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nxt = (current[0] + dr, current[1] + dc)
            if not (0 <= nxt[0] < rows and 0 <= nxt[1] < cols):
                continue
            if grid[nxt[0]][nxt[1]] == 1:
                continue
            new_cost = cost_so_far[current] + 1
            if new_cost < cost_so_far.get(nxt, float("inf")):
                cost_so_far[nxt] = new_cost
                came_from[nxt] = current
                priority = new_cost + heuristic(nxt, goal)
                heapq.heappush(open_heap, (priority, new_cost, nxt))
    return None

if __name__ == "__main__":
    warehouse_grid = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    path = a_star(warehouse_grid, (0, 0), (4, 4))
    print("Optimal Path:", path)
