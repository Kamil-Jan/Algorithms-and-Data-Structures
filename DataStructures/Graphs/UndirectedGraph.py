from collections import deque


class Graph(object):
    def __init__(self, graph_dict=dict()):
        self.__graph_dict = graph_dict

    def vertices(self):
        """
        Returns the vertices of a graph.
        """
        return list(self.__graph_dict.keys())

    def add_vertex(self, vertex):
        """
        If the vertex "vertex" is not in
        self.__graph_dict, a key "vertex" with an empty
        list as a value is added to the dictionary.
        Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def vertex_degree(self, vertex):
        """
        The degree of a vertex is the number of edges connecting
        it, i.e. the number of adjacent vertices. Loops are counted
        double, i.e. every occurence of vertex in the list
        of adjacent vertices.
        """
        adj_vertices = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def degree_sequence(self):
        """
        Calculates the degree sequence.
        """
        seq = []
        for vertex in self.__graph_dict:
            seq.append(self.vertex_degree(vertex))
        seq.sort(reverse=True)
        return tuple(seq)

    @staticmethod
    def erdos_gallai(dsequence):
        """
        Whether a given degree sequence can be realized
        by a simple graph. Erdos Gallai theorem.
        """
        if sum(dsequence) % 2:
            return False
        for k in range(1, len(dsequence) + 1):
            left = sum(dsequence[:k])
            right =  k * (k - 1) + sum([min(x, k) for x in dsequence[k:]])
            if left > right:
                return False
        return True

    def find_isolated_vertices(self):
        """
        Returns a list of isolated vertices.
        """
        isolated = []
        for vertex in self.__graph_dict:
            if not self.__graph_dict[vertex]:
                isolated.append(vertex)
        return isolated

    def delta(self):
        """
        The minimum degree of the vertices.
        """
        minimum = float("inf")
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree < minimum:
                minimum = vertex_degree
        return minimum

    def Delta(self):
        """
        The maximum degree of the vertices.
        """
        maximum = 0
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > maximum:
                maximum = vertex_degree
        return maximum

    def edges(self):
        """
        Returns the edges of a graph.
        """
        return self.__generate_edges()

    def add_edge(self, edge):
        """
        Assumes that edge is of type set, tuple or list;
        between two vertices can be multiple edges!
        """
        vertex1, vertex2 = edge
        self.__add_edge_into_dict(vertex1, vertex2)
        self.__add_edge_into_dict(vertex2, vertex1)

    def __add_edge_into_dict(self, from_vertex, to_vertex):
        if from_vertex in self.__graph_dict:
            self.__graph_dict[from_vertex].append(to_vertex)
        else:
            self.__graph_dict[from_vertex] = [to_vertex]

    def density(self):
        """
        Method to calculate the density of a graph.
        """
        V = len(self.vertices())
        E = len(self.edges())
        return 2.0 * E / (V *(V - 1))

    def find_path(self, start, end, path=[]):
        """
        Find a path from start_vertex to end_vertex
        in graph.
        """
        path = path + [start]
        if start == end:
            return path
        if not self.__graph_dict[start]:
            return None
        for node in self.__graph_dict[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath
        return None

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not self.__graph_dict[start]:
            return []
        paths = []
        for node in self.__graph_dict[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_shortest_path(self, start, end):
        dist = {start: [start]}
        q = deque(start)
        while len(q):
            at = q.popleft()
            for next in self.__graph_dict[at]:
                if next not in dist:
                    dist[next] = [dist[at], next]
                    q.append(next)
        return dist.get(end)

    def diameter(self):
        """
        Calculates the diameter of the graph.
        """

        v = self.vertices()
        pairs = [(v[i], v[j]) for i in range(len(v) - 1) for j in range(i + 1, len(v))]
        smallest_paths = []
        for s, e in pairs:
            paths = self.find_all_paths(s,e)
            smallest = sorted(paths, key=len)[0]
            smallest_paths.append(smallest)

        smallest_paths.sort(key=len)

        # longest path is at the end of list,
        # i.e. diameter corresponds to the length of this path
        diameter = len(smallest_paths[-1]) - 1
        return diameter

    def __generate_edges(self):
        """
        A static method generating the edges of the
        graph. Edges are represented as sets
        with one or two vertices.
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += f"{k} "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += f"{edge} "
        return res


def main():
    g = {"a": ["c"],
         "b": ["c","e","f"],
         "c": ["a","b","d","e"],
         "d": ["c"],
         "e": ["b","c","f"],
         "f": ["b","e"]}

    complete_graph = {"a": ["b","c"],
                      "b": ["a","c"],
                      "c": ["a","b"]}

    G = Graph(g)
    CG = Graph(complete_graph)
    print(G.density())
    print(CG.density())
    print(G.diameter())
    print(CG.diameter())

if __name__ == "__main__":
    main()

