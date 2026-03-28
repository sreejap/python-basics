"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs (start_node):
            if start_node is None:
                return start_node
            
            if start_node in visited:
                return visited[start_node]
            
            clone = Node(start_node.val)
            visited[start_node]=clone # mark as visited before calling on nghbrs
            for nei in start_node.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone # we have to return    

        clone_graph = dfs (node)
        return clone_graph
