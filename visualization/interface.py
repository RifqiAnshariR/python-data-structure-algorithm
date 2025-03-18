import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithm.bfs_dsa import GraphBFS
from algorithm.dfs_dsa import GraphDFS
from algorithm.astar_dsa import GraphAStar

# Penggunaan
graph = GraphBFS()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(2, 3)
graph.addEdge(3, 3)

print("\nBFS traversal:")
print(graph.graph)
graph.bfs(2)  # Output: 2 0 3 1