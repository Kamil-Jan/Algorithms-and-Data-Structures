import Graph
import networkx as nx
from matplotlib.pyplot import show


def is_valid(graph: Graph.Graph, vertex: Graph.Vertex, color):
    for neighbor in vertex.get_connections():
        neighbor = graph.get_vertex(neighbor)
        try:
            if neighbor.color == color:
                return False
        except:
            pass
    return True

def choose_color(graph: Graph.Graph, cur_vertex: Graph.Vertex, colors: list):
    for color in colors:
        if is_valid(graph, cur_vertex, color):
            return color

def color(graph: Graph.Graph, colors: list, start_vertex=None):
    graph_vertices = graph.vertices()
    for vertex in graph_vertices:
        vertex = graph.get_vertex(vertex)
        vertex.color = choose_color(graph, vertex, colors)
        if not vertex.color:
            return False
    return True

def draw(graph):
    if graph.directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    vertices = graph.vertices()
    edge_labels = graph.edges()
    edges = list(edge_labels.keys())
    G.add_edges_from(edges)

    layout = nx.spring_layout(G)
    nx.draw(G, layout)
    nx.draw_networkx_nodes(G, pos=layout,
                           nodelist=[vertex for vertex in vertices],
                           node_color=[graph.get_vertex(vertex).color for vertex in vertices])
    nx.draw_networkx_labels(G, pos=layout, font_color="white")
    nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=edge_labels)
    show()

if __name__ == "__main__":
    g = Graph.Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(1, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 3)
    g.add_edge(4, 5)
    colors = ["red","green","blue","yellow"]
    if color(g, colors):
        for vertex in g.vertices():
            vertex = g.get_vertex(vertex)
            print(vertex.id, vertex.color)
        draw(g)

