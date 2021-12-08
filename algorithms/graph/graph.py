

class Graph:
    class Vertex:
        __slots__ = "_element"

        def __init__(self, x):
            self._element = x

        def element(self):
            return self._element

        def __hash__(self):
            return hash(id(self))
        
        def __str__(self):
            return self._element


    class Edge:
        _slots__ = '_orgin', '_destination', '_element'

        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            return (self._origin, self._destination)

        def opposite(self, v):
            return self._destination if v is self._origin else self._origin

        def element(self):
            return self._element

        def __hash__(self):
            return hash((self._origin, self._destination))

        def __str__(self):
            return str(self._origin) + ' ---> ' + str(self._destination)

    """init for graph"""
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v] for v in self._outgoing.key()))
        return total if self.is_directed() else total // 2
    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edges(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self,v,outgoing =True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])  

    def incident_edges(self,v,outgoing = True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
    
    def insert_vertex(self, x = None):
        v = self.Vertex(x)
        self._outgoing[v] ={}
        if self.is_directed():
            self._incoming[v] = {}
        return v
    def insert_edge(self,u,v,x = None):
        e = self.Edge(u,v,x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e




if __name__ == "__main__":
    g = Graph()
    bos = g.insert_vertex('BOS')
    jfk = g.insert_vertex('JFK')
    ord = g.insert_vertex('ORD')
    dfw = g.insert_vertex('DFW')
    mia = g.insert_vertex('MIA')
    lax = g.insert_vertex('LAX')
    sfo = g.insert_vertex('SFO')

    g.insert_edge(bos, jfk)
    g.insert_edge(bos, sfo)
    g.insert_edge(bos, mia)
    g.insert_edge(jfk,bos)
    g.insert_edge(jfk,mia)
    g.insert_edge(jfk,sfo)
    g.insert_edge(jfk,dfw)
    g.insert_edge(dfw,ord)
    g.insert_edge(dfw,sfo)
    g.insert_edge(dfw,lax)
    g.insert_edge(ord,mia)
    g.insert_edge(ord,dfw)
    g.insert_edge(lax,ord)
    g.insert_edge(sfo,lax)
    g.insert_edge(mia,dfw)
    g.insert_edge(mia, lax)

