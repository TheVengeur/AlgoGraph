import networkx as nx
import matplotlib.pyplot as plt


def find_eurelian(graph):
    print(graph.degree)
    print(graph.edges)
    vertex_degrees = graph.degree
    odd_degree = 0
    odd_vertex = None
    for v_degree in vertex_degrees:
        if v_degree[1] == 0:
            return None
        odd_degree += v_degree[1] % 2
        if odd_vertex is None and v_degree[1] % 2 == 1:
            odd_vertex = v_degree[0]
    if odd_degree != 0 and odd_degree != 2:
        return None
    current_node = None
    if odd_vertex is not None:
        current_node = odd_vertex
    else:
        current_node = next(iter(graph.nodes))
    path = []

    edges = [(edge[0], edge[1], False) for edge in graph.edges]
    while True:

        new_edges = list(
            filter(lambda edge: (edge[0] == current_node or edge[1] == current_node) and edge[2] is False, edges))
        if not new_edges:
            if list(filter(lambda edge: edge[2] is False, edges)) is not None:
                return path
            else:
                print(path)
                return None
        for e in new_edges:
            if (e[0] == current_node and odd_vertex is not None) or len(new_edges) >= 1:
                edge = e
                break
        idx = edges.index(edge)
        edges.insert(edges.index(edge), (edge[0], edge[1], True))
        edges.pop(idx + 1)
        path.append((edge[0], edge[1]))
        current_node = edge[not edge.index(current_node)]

def is_eurelian(graph):
    if find_eurelian(graph):
        return True
    return False


def find_hamiltonian(graph, current_node, visited_nodes, path):
    print("path: {}".format(path))

    if len(path) == len(graph.nodes):
        return path

    for node in graph.neighbors(current_node):
        if node not in visited_nodes:
            visited_nodes.add(node)
            path.append(node)
            result = find_hamiltonian(graph, node, visited_nodes.copy(), path.copy())  # Recursive call
            if result:
                return result
            visited_nodes.remove(node)
            path.pop()

    return None


def is_hamiltonian(graph):
    visited_nodes = set()
    visited_nodes.add(next(iter(graph.nodes)))
    path = [next(iter(graph.nodes))]
    return find_hamiltonian(graph, path[0], visited_nodes, path)


def test_eulerian():
    count = 0
    for i in range(10):
        G = nx.erdos_renyi_graph()
        t = nx.has_eulerian_path(G)
        tt = is_eurelian(G)
        if (t is None and tt is None) or (t is not None and tt is not None):
            count += 1
    return count


def graph_to_plot(graph, name, figure_number):
    plt.subplot(1, 2, figure_number)
    nx.draw(graph, with_labels=name)
    plt.title(name)
    is_eulerian = is_eurelian(graph)
    plt.figtext(0.10 + (0.4 * (figure_number - 1)), 0.90, "isEulerian={}".format(is_eurelian(graph)))
    if is_eulerian:
        plt.figtext(0 + (0.5 * (figure_number - 1)), 0.10, "Eulerien={}".format(find_eurelian(graph)))
    if is_hamiltonian(graph) is None:
        is_hamilton = False
    else:
        is_hamilton = True
    plt.figtext(0.10 + (0.4 * (figure_number - 1)), 0.85, "isHamiltonian={}".format(is_hamilton))
    if is_hamilton:
        plt.figtext(0 + (0.5 * (figure_number - 1)), 0.05, "Hamiltonian={}".format(is_hamiltonian(graph)))


def start():
    G = nx.erdos_renyi_graph(5, 0.5)
    LG = nx.line_graph(G)
    graph_to_plot(G, "G", 1)
    graph_to_plot(LG, "LG", 2)
    plt.figure(figsize=(10, 4))
    plt.show()
