from graph import Graph

"""
DFO is depth first. You take a vertex, loop through its incident edges, take the first one, find the opposte vertex,
if its not discovered, add it into the dictionary and use that vertex and recurse
"""

def DFS(g, u, discovered):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            print('indicents for', u, 'oppsite', v, e)
            discovered[v] = e
            DFS(g, v, discovered)


if __name__ == "__main__":
    g = Graph(directed=True)
    bos = g.insert_vertex('BOS')
    jfk = g.insert_vertex('JFK')
    ord = g.insert_vertex('ORD')
    dfw = g.insert_vertex('DFW')
    mia = g.insert_vertex('MIA')
    lax = g.insert_vertex('LAX')
    sfo = g.insert_vertex('SFO')
    dxb = g.insert_vertex('DXB')
    per = g.insert_vertex('PER')

    g.insert_edge(bos, jfk)
    g.insert_edge(bos, sfo)
    g.insert_edge(bos, mia)
    g.insert_edge(jfk, bos)
    g.insert_edge(jfk, mia)
    g.insert_edge(jfk, sfo)
    g.insert_edge(jfk, dfw)
    g.insert_edge(dfw, ord)
    g.insert_edge(dfw, sfo)
    g.insert_edge(dfw, lax)
    g.insert_edge(ord, mia)
    g.insert_edge(ord, dfw)
    g.insert_edge(lax, ord)
    g.insert_edge(sfo, lax)
    g.insert_edge(mia, dfw)
    g.insert_edge(mia, lax)

    g.insert_edge(dxb, per)
    # g.insert_edge(dxb, mia)

    result = {bos: None}
    DFS(g, bos, result)
    for k in result.keys():
        print(k)
