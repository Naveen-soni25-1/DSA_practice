graph = {}
graph["start"] = {"a": 6, "b": 2}
graph["a"] = {"fin": 1}
graph["b"] = {"a": 3, "fin": 5}
graph["fin"] = {} # edges relation with weights

infinity = float("inf")

# Cost table
costs = {
    "a": 6,
    "b": 2,
    "fin": infinity
}

# Parent table
parents = {
    "a": "start",
    "b": "start",
    "fin": None
}

# List to keep track of processed nodes
processed = []

# Helper function to find the lowest-cost unprocessed node
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # keys
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Dijkstra’s Algorithm Core Logic
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

# Output the final cost table and path
print("Costs:", costs)
print("Parents:", parents)