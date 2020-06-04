import Graph


def DFS(graph: Graph.Graph, cur_vertex, depth: int = 1):
    cur_vertex = graph.get_vertex(cur_vertex)
    cur_vertex.visited = True
    cur_vertex.discovery_time = depth
    cur_vertex.low = depth
    vertex_children = 0

    art_points = []
    for neighbor in cur_vertex.get_connections():
        neighbor = graph.get_vertex(neighbor)
        if not neighbor.visited:
            neighbor.parent = cur_vertex
            vertex_children += 1
            art_points.extend(DFS(graph, neighbor.id, depth + 1))

            cur_vertex.low = min(cur_vertex.low, neighbor.low)
            if cur_vertex.parent and neighbor.low >= cur_vertex.discovery_time:
                if cur_vertex.id not in art_points:
                    art_points.append(cur_vertex.id)
        elif neighbor != cur_vertex.parent:
            cur_vertex.low = min(cur_vertex.low, neighbor.discovery_time)

    if depth == 1 and vertex_children > 1:
        art_points.append(cur_vertex.id)

    return art_points

def art_points(graph, root=None):
    if not root:
        root = graph.vertices()[0]

    graph.get_vertex(root).parent = None
    for vertex in graph.vertices():
        vertex = graph.get_vertex(vertex)
        vertex.visited = False
    return DFS(graph, root)

if __name__ == "__main__":
    print("module imported")
    g = Graph.Graph()
    g.add_edge(1, 0)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 3)
    g.add_edge(0, 6)
    g.add_edge(6, 5)
    g.add_edge(5, 7)
    g.add_edge(5, 8)
    g.add_edge(7, 8)
    g.add_edge(8, 9)
    g.add_edge(10, 11)
    g.add_edge(10, 12)
    print(art_points(g))

