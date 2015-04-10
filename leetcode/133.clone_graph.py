# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None

        nh = set()
        head = UndirectedGraphNode(node.label)
        nd = {node.label: head}
        od = {node.label: node}

        stack = [node.label]

        while stack:
            label = stack.pop()
            if label in nh:
                continue
            nh.add(label)
            target = nd[label]
            ori = od[label]

            for nei in ori.neighbors:
                if not nei.label in nh:
                    stack.append(nei.label)
                od[nei.label] = nei
                if not nd.has_key(nei.label):
                    nd[nei.label] = UndirectedGraphNode(nei.label)
                target.neighbors.append(nd[nei.label])
        return head
