import sys


def traveling_util(graph: list, paths_table: dict, i, vertices_left: list, path=[]):
    if not vertices_left:
        return paths_table[(i, ())]
    for k in vertices_left:
        remain_vertices = tuple([vertex for vertex in vertices_left if vertex != k])
        prev_cost, new_path = traveling_util(graph, paths_table,
                                             k, remain_vertices)
        new_cost = graph[i][k] + prev_cost
        if new_cost < paths_table.get((i, vertices_left), (float("inf"), []))[0]:
            paths_table[(i, vertices_left)] = (new_cost, [i] + new_path)
    return paths_table[(i, vertices_left)]

def traveling(graph):
    n = len(graph)
    paths_table = {(i, ()): (graph[i][0], [i, 0]) for i in range(1, n)}
    remain_vertices = tuple(range(1, n))
    traveling_util(graph, paths_table, 0, remain_vertices)
    return paths_table[(0, remain_vertices)]

if __name__ == "__main__":
    g = [[0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571],
         [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403],
         [713, 1745, 0, 355, 920, 803, 1737, 851, 1858],
         [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584],
         [1631, 831, 920, 700, 0, 663, 1021, 1769, 949],
         [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765],
         [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678],
         [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699],
         [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0]]
    print(traveling(g))

