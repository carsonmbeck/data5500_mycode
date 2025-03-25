# ChatGPT prompt snippet:
# "How do I count the number of nodes in a NetworkX graph?"

import networkx as nx

def count_nodes(graph: nx.Graph) -> int:
    """
    Returns the number of nodes in the given NetworkX graph.
    """
    return graph.number_of_nodes()

# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3])
    print("Number of nodes in the graph:", count_nodes(G))
