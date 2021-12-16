from graph_gen import GenerateGraph
"""
DFO is depth first. You take a vertex, loop through its incident edges, take the first one, find the opposte vertex,
if its not discovered, add it into the dictionary and use that vertex and recurse

BFS is good for finding shortest path
DFS is good for game simulations to look for a path to the result.
"""

def BFS(g,s,discovered):
    level =[s]
    while len(level) >0:
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] =e
                    next_level.append(v)
        level = next_level

def DFS(g, u, discovered):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            print('indicents for', u, 'oppsite', v, e)
            discovered[v] = e
            DFS(g, v, discovered)


if __name__ == "__main__":
    (g, v) = GenerateGraph()

    print("-------DFS----------")
    result = {v[0]: None}
    DFS(g, v[0], result)
    for k in result.keys():
        print(k)

    print("-------BFS----------")
    result = {v[0]: None}
    BFS(g, v[0], result)
    for k in result.keys():
        print(k)
