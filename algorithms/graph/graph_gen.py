from graph import Graph


def GenerateWeightedGraph():
    g = Graph()
    v = []
    bos = g.insert_vertex('BOS')
    jfk = g.insert_vertex('JFK')
    ord = g.insert_vertex('ORD')
    dfw = g.insert_vertex('DFW')
    mia = g.insert_vertex('MIA')
    lax = g.insert_vertex('LAX')
    sfo = g.insert_vertex('SFO')

    v.append(bos)
    v.append(jfk)
    v.append(ord)
    v.append(dfw)
    v.append(mia)
    v.append(lax)
    v.append(sfo)

    g.insert_edge(bos, jfk, 187)
    g.insert_edge(bos, sfo, 2704)
    g.insert_edge(bos, ord, 867)
    g.insert_edge(bos, mia, 1258)
    g.insert_edge(jfk, mia, 1090)
    g.insert_edge(jfk, ord, 740)
    g.insert_edge(dfw, ord, 802)
    g.insert_edge(dfw, sfo, 1464)
    g.insert_edge(dfw, lax, 1235)
    g.insert_edge(dfw, mia, 1121)
    g.insert_edge(ord, sfo, 1846)
    g.insert_edge(lax, sfo, 337)
    g.insert_edge(lax, mia, 2342)

    return (g, v)


def GenerateGraph():
    g = Graph(directed=True)
    v = []
    bos = g.insert_vertex('BOS')
    jfk = g.insert_vertex('JFK')
    ord = g.insert_vertex('ORD')
    dfw = g.insert_vertex('DFW')
    mia = g.insert_vertex('MIA')
    lax = g.insert_vertex('LAX')
    sfo = g.insert_vertex('SFO')
    dxb = g.insert_vertex('DXB')
    per = g.insert_vertex('PER')

    v.append(bos)
    v.append(jfk)
    v.append(ord)
    v.append(dfw)
    v.append(mia)
    v.append(lax)
    v.append(sfo)
    v.append(dxb)
    v.append(per)

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

    return (g, v)
