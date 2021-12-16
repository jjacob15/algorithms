from graph_gen import GenerateWeightedGraph
def getMin(m):
    c = float('inf')
    r = None
    for v in m.keys():
        if m[v] <= c:
            c = m[v]
            r = v
    del m[r]
    return r


def shortest_path_lengths(g,src):
    cost = {}
    focused_vertex = src
    
    for v in g.vertices():
        if v is src:
            cost[v] = 0
        else:
            cost[v] = float('inf')

    accessed_edges = []
    pending_edges = {}
    pending_edges[focused_vertex] = 0

    while len(pending_edges) > 0:
        min_edge = getMin(pending_edges)
        print('closest edge', min_edge)
        
        for edge in g.incident_edges(min_edge):
            opposite = edge.opposite(min_edge)
            wgt = edge.element()

            if cost[min_edge] + wgt < cost[opposite]:
                cost[opposite] = cost[min_edge] + wgt
                print('cost to ', opposite, cost[opposite])

            if opposite not in accessed_edges:
                pending_edges[opposite] = cost[opposite]
                accessed_edges.append(opposite)

    print(len(cost))
    for k in cost.keys():
        print(k, cost[k])
            
    # while len(g.incident_edges(focused_vertex)) > 0:
    #     u = getMin(q)
    #     print('processing ', u)
    #     cloud[u] = u

    #     for e in g.incident_edges(u):
    #         # print(u, e)
    #         v = e.opposite(u)
    #         if v not in cloud:
    #             wgt = e.element()
    #             print(wgt, v, u)
    #             if d[u] + wgt < d[v]:
    #                 print('relaxing', v, ' with ', u, d[u], wgt, d[u]+wgt)
    #                 d[v] = d[u]+wgt
    #                 f[v] = d[u]+wgt
                    

    # print(len(f))
    # for v in f.keys():
    #     print(f[v], v)
        

    
    

if __name__ == "__main__":
    (g, v) = GenerateWeightedGraph()
    s = shortest_path_lengths(g, v[0])
