class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rep = [i for i in range(n + 1)]

        def find(node):
            if rep[node] == node:
                return node
            
            parent = find(rep[node])
            rep[node] = parent
            return parent
        
        def union(a, b):
            rep_a = find(a)
            rep_b = find(b)

            if rep_a == rep_b:
                return False

            rep[rep_b] = rep_a
            return True
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
        
