from collections import deque


class Vertex(object):
    def __init__(self, val=None):
        self.val = val
        self.adjacent = dict()

    def add_neighbor(self, neighbour, weight=0):
        self.adjacent[neighbour] = weight

    def get_connections(self):
        return list(self.adjacent.keys())

    def get_weight(self, neighbour):
        return self.adjacent[neighbour]


class Graph(object):
    def __init__(self, graph_dict=None, directed=False):
        self.__graph_dict = dict()
        self.directed = directed
        if graph_dict:
            self.__generate_dict(graph_dict)

    def vertices(self):
        """
        Returns the vertices of a graph.
        """
        return list(self.__graph_dict.keys())

    def add_vertex(self, vertex, val=None):
        """
        If the vertex is not in self.__graph_dict,
        an instance of a class Vertex is added to the dictionary.
        Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            new_vertex = Vertex(val)
            self.__graph_dict[vertex] = new_vertex
            return vertex

    def get_vertex(self, vertex):
        """
        Returns Vertex class instance of a given vertex.
        """
        if vertex in self.__graph_dict:
            return self.__graph_dict[vertex]

    def vertex_degree(self, vertex):
        """
        The degree of a vertex is the number of edges connecting
        it, i.e. the number of adjacent vertices. Loops are counted
        double, i.e. every occurence of vertex in the list
        of adjacent vertices.
        """
        adj_vertices = self.__graph_dict[vertex].get_connections()
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def find_isolated_vertices(self):
        """
        Returns a list of isolated vertices.
        """
        isolated = []
        for vertex in self.__graph_dict:
            if not self.__graph_dict[vertex].get_connections():
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

    def add_edge(self, frm, to, weight=0):
        """
        Adds an edge into a graph.
        """
        if frm not in self.__graph_dict:
            frm = self.add_vertex(frm)
        if to not in self.__graph_dict:
            to = self.add_vertex(to)

        self.__graph_dict[frm].add_neighbor(to, weight)
        if not self.directed:
            self.__graph_dict[to].add_neighbor(frm, weight)

    def find_path(self, start, end, path=[]):
        """
        Finds a path from 'start' to 'end' in graph.
        May not be shortest.
        """
        path = path + [start]
        if start == end:
            return path
        if not self.__graph_dict[start]:
            return None
        for node in self.__graph_dict[start].get_connections():
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath
        return None

    def find_all_paths(self, start, end, path=[]):
        """
        Finds all possible paths from 'start' to 'end'.
        """
        path = path + [start]
        if start == end:
            return [path]
        if not self.__graph_dict[start]:
            return []
        paths = []
        for node in self.__graph_dict[start].get_connections():
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_all_paths_except(self, start, end, ignore, path=[]):
        """
        Finds all possible paths from 'start' to 'end'.
        """
        path = path + [start]
        if start == end:
            return [path]
        if not self.__graph_dict[start]:
            return []
        paths = []
        for node in self.__graph_dict[start].get_connections():
            if node not in path and node != ignore:
                newpaths = self.find_all_paths_except(node, end, ignore, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_all_paths_include(self, start, end, include):
        paths = self.find_all_paths(start, end)
        for key, path in enumerate(paths):
            if include not in path:
                del paths[key]
        return paths

    def find_shortest_path(self, start, end):
        """
        Finds shortest path from 'start' to 'end'.
        """
        dist = {start: [start]}
        q = deque(start)
        while len(q):
            at = q.popleft()
            for next in self.__graph_dict[at].get_connections():
                if next not in dist:
                    dist[next] = [dist[at], next]
                    q.append(next)
        return dist.get(end)

    def __generate_dict(self, graph_dict):
        """
        Generates self.__graph_dict from 'graph_dict'.
        """
        for vertex in graph_dict:
            self.add_vertex(vertex)
            for neighbor in graph_dict[vertex]:
                self.add_edge(vertex, neighbor)

    def __generate_edges(self):
        """
        Generates the edges of the graph.
        Edges are represented as tuples
        with one or two vertices.
        """
        edges = []
        if not self.directed:
            for vertex in self.__graph_dict:
                for neighbour in self.__graph_dict[vertex].get_connections():
                    if (neighbour, vertex) not in edges:
                        edges.append((vertex, neighbour))
        else:
            for vertex in self.__graph_dict:
                for neighbour in self.__graph_dict[vertex].get_connections():
                    edges.append((vertex, neighbour))
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
    g = {"A": ["B", "C","D"],
         "B": ["D","K"],
         "C": ["D","K"],
         "D": ["K"],
         "F": []}

    G = Graph(g, directed=True)
    print(len(G.find_all_paths("B","K")))

if __name__ == "__main__":
    main()

