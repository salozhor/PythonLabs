import networkx as nx
import networkx.classes.graph
import matplotlib.pyplot as plt
from networkx.algorithms.bipartite.basic import color
from networkx.algorithms.traversal.edgedfs import helper_funcs, edge_dfs

def find_cycle(G, source=None):
    orientation='original'
    out_edge, key, tailhead = helper_funcs(G, orientation)

    explored = set()
    cycle = []
    final_node = None
    for start_node in G.nbunch_iter(source):

        if start_node in explored:
            # No loop is possible.
            continue

        edges = []
        # All nodes seen in this iteration of edge_dfs
        seen = {start_node}
        # Nodes in active path.
        active_nodes = {start_node}
        previous_node = None
        for edge in edge_dfs(G, start_node, orientation):
            # Determine if this edge is a continuation of the active path.
            tail, head = tailhead(edge)
            if previous_node is not None and tail != previous_node:
                """ This edge results from backtracking.
                Pop until we get a node whose head equals the current tail.
                So for example, we might have:
                    (0,1), (1,2), (2,3), (1,4)
                which must become:
                    (0,1), (1,4)
				"""
                while True:
                    try:
                        popped_edge = edges.pop()
                    except IndexError:
                        edges = []
                        active_nodes = {tail}
                        break
                    else:
                        popped_head = tailhead(popped_edge)[1]
                        active_nodes.remove(popped_head)

                    if edges:
                        last_head = tailhead(edges[-1])[1]
                        if tail == last_head:
                            break

            edges.append(edge)

            if head in active_nodes:
                # We have a loop!
                cycle.extend(edges)
                final_node = head
                break
            elif head in explored:
                # Then we've already explored it. No loop is possible.
                break
            else:
                seen.add(head)
                active_nodes.add(head)
                previous_node = head

        if cycle:
            break
        else:
            explored.update(seen)

    else:
        assert(len(cycle) == 0)
        raise nx.exception.NetworkXNoCycle('No cycle found.')

    # We now have a list of edges which ends on a cycle.
    # So we need to remove from the beginning edges that are not relevant.

    for i, edge in enumerate(cycle):
        tail, head = tailhead(edge)
        if tail == final_node:
            break

    return cycle[i:]

def is_bipartite(G):
    """ Returns True if graph G is bipartite, False if not.

    Parameters
    ----------
    G : NetworkX graph

    Examples
    --------
    >>> from networkx.algorithms import bipartite
    >>> G = nx.path_graph(4)
    >>> print(bipartite.is_bipartite(G))
    True

    See Also
    --------
    color, is_bipartite_node_set
    """
    try:
        color(G)
        return True
    except nx.NetworkXError:
        return False
	
	
G=nx.Graph()


"""
Node describing
"""
G.add_node('a')
G.add_node('b')
G.add_node('c')
G.add_node('d')
G.add_node('e')

"""
Edge describing
"""
G.add_edge('a','b')
G.add_edge('c','b')
G.add_edge('a','e')
G.add_edge('b','d')
#G.add_edge('c','d')

"""
"Double degree" 
"""
adj = nx.adjacency_matrix(G)
a = adj.toarray()
q = [0 for qew in range(len(a))]
for i in range(len(a)):
	for j in range(len(a[i])):
		if a[i][j]==1:
			for k in range(len(a[j])):
				q[i]+=a[j][k]
print(q)
print(a)

"""
cycle
"""
try:
	print(find_cycle(G, source='a'))*
except nx.exception.NetworkXNoCycle:
	print("There is no cycle")
"""
Bipartite
"""
print("Is this graph bipartite?", is_bipartite(G))

"""
Draw
"""
nx.draw(G, with_labels = True)
plt.draw()
plt.show()