"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        adj = defaultdict(list)
        node_map = {}

        queue = deque([node])
        visited = set([node.val])

        while queue:
            curr = queue.popleft()
            node_map[curr.val] = Node(curr.val)
            for nei in curr.neighbors:
                adj[curr.val].append(nei.val)
                if nei.val not in visited:
                    queue.append(nei)
                visited.add(nei.val)
        
        for src, dsts in adj.items():
            for dst in dsts:
                node_map[src].neighbors.append(node_map[dst])
        
        return node_map[1]
        
        

