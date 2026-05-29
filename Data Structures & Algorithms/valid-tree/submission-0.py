from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
            
        # Build the adjacency list
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        visit = set()
        
        # DFS helper function to detect cycles
        def dfs(node, prev):
            # If the node is already visited, a cycle is detected
            if node in visit:
                return False
            
            visit.add(node)
            
            # Recursively visit neighbors
            for neighbor in adj[node]:
                # Skip the node we just came from to avoid false positive cycles
                if neighbor == prev:
                    continue
                    
                if not dfs(neighbor, node):
                    return False
                    
            return True
            
        # 1. dfs(0, -1) ensures there are no cycles
        # 2. len(visit) == n ensures all nodes are connected (no isolated components)
        return dfs(0, -1) and len(visit) == n