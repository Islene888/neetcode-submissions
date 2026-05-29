from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find(node):
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]  # 只有路径压缩
                res = parent[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
                
            parent[p2] = p1  
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
            
        return res