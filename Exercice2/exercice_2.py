import time
import networkx as nx
import matplotlib.pyplot as plt


def maximum_degree(graph):
    sorted_nodes = sorted(graph.degree, key=lambda x: x[1], reverse=True)
    pairs = []
    found_node = set()

    for node, _ in sorted_nodes:
        if node in found_node:
            continue
        pair = next(filter(lambda n: n not in found_node, graph.neighbors(node)), None)
        if pair is not None:
            pairs.append((node, pair))
            found_node.add(node)
            found_node.add(pair)
    return pairs

def minimum_degree(graph):
    sorted_nodes = sorted(graph.degree, key=lambda x: x[1])
    pairs = []
    found_node = set()

    for node, _ in sorted_nodes:
        if node in found_node:
            continue
        pair = next(filter(lambda n: n not in found_node, graph.neighbors(node)), None)
        if pair is not None:
            pairs.append((node, pair))
            found_node.add(node)
            found_node.add(pair)
    return pairs


def generate_plot(function, trials, name):
    computation_times = []
    results = []
    mean_results = []
    mean_times = []

    for i in range(trials):
        graph = nx.gnp_random_graph(trials, 0.04)
        start_time = time.time()
        result = len(function(graph))
        computation_times.append(time.time() - start_time)
        results.append(result)
        mean_results.append(sum(results) / (i + 1))
        mean_times.append(sum(computation_times) / (i + 1))



    plt.subplot(1, 2, 1)
    plt.plot(list(range(1, trials + 1)), mean_results, "-", label=name, scaley=True)
    plt.subplot(1, 2, 2)
    plt.plot(list(range(1, trials + 1)), mean_times, "-", label=name, scaley=True)


def run():
    plt.figure(figsize=(14, 6))

    graph = nx.gnp_random_graph(120, 0.04)
    generate_plot(nx.maximal_matching, 200, "ref")

    generate_plot(maximum_degree, 200, "maximum degree heuristic")
    generate_plot(minimum_degree, 200, "minimum degree heuristic")
    plt.subplot(1, 2, 1)
    plt.title('Mean matching size')
    plt.ylabel('Matching means evolution')
    plt.xlabel('trials')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.title('Mean matching size computation time evolution')
    plt.ylabel('Computation time')
    plt.xlabel('trials')
    plt.legend()
    plt.show()


run()
