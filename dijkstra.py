
#       1     3     5
#     _____a_____c______
#    |     |     |      |
# start    | 2   | 3    fin
#    |_____b_____d______|
#       4     4      2



graph = {
    'start': {'a': 1, 'b': 4}, 
    'a': {'b':2, 'c': 3}, 
    'b': {'d': 4}, 
    'c': {'fin': 5},
    'd': {'c': 3, 'fin': 2},
    'fin': {}
    } 



infinity = float("inf")

costs = {
    'a': 1, 
    'b': 4, 
    'c': infinity,
    'd': infinity,
    'fin': infinity
    }


parents = {
    'a': 'start', 
    'b': 'start', 
    'c': None,
    'd': None,
    'fin': None
    }


processed = ["start", ]

def search():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for i in neighbours.keys():
            new_cost = cost + neighbours[i] #if it's cheaper to go to this neighbour
            if costs[i] > new_cost:         #by going through this node 
                costs[i] = new_cost         #update the cost of this node
                parents[i] = node           #this node becomes a parent for this neighbour
        processed.append(node)
        node = find_lowest_cost_node(costs)


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def path(start, finish):
    search()
    path_ = [finish, ]
    processing = finish
    while start not in path_:
        for node, parent in parents.items():
            if node == processing:
                path_.append(parent)
                processing = parent
    return path_[::-1]

print(path('start', 'd'))
