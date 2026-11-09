# Warehouse graph represented as an adjacency list
warehouse_graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def dfs(graph, start, goal):
    visited = set()

    def search(node, path):
        visited.add(node)
        path = path + [node]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                result = search(neighbor, path)
                if result is not None:
                    return result
        return None

    return search(start, [])

if __name__ == "__main__":
    start_node, goal_node = "A", "F"
    path = dfs(warehouse_graph, start_node, goal_node)
    if path:
        print(f"DFS Path from {start_node} to {goal_node}: " + " -> ".join(path))
    else:
        print("No path found")
