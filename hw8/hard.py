# ChatGPT prompt snippet:
# "What is a good way to count nodes with a high degree in a NetworkX graph?"

import networkx as nx

def count_high_degree_nodes(graph: nx.Graph, threshold: int = 5) -> int:
    """
    Returns the number of nodes in the given NetworkX graph that have a degree greater than the specified threshold (default is 5).
    """
    count = 0
    for node, degree in graph.degree():
        if degree > threshold:
            count += 1
    return count

# Example usage:
if __name__ == "__main__":
    # Create a sample graph with varying node degrees
    G = nx.Graph()
    # Adding edges so that one node has a high degree
    G.add_edges_from([
        (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
        (2, 8), (2, 9), (3, 10)
    ])
    print("Number of nodes with degree > 5:", count_high_degree_nodes(G))
