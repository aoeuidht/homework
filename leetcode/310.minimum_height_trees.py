class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]
        edge_map = {}
        for h, t in edges:
            edge_map.setdefault(h, [])
            edge_map.setdefault(t, [])
            edge_map[h].append(t)
            edge_map[t].append(h)

        # build the tree
        start_node, tree_height, tree = self.dfs(edge_map, edges[0][0])

        max_node, max_height = start_node, tree_height
        for node, sub_node_list in tree.iteritems():
            if len(sub_node_list) > 1:
                if sub_node_list[0][1] + sub_node_list[1][1] + 1 > max_height:
                    max_node, max_height = node, sub_node_list[0][1] + sub_node_list[1][1] + 1

        # dfs generate path
        if max_node == start_node:
            tree_path = self.dfs_path(tree, start_node)
        else:
            tree_path = self.dfs_path(tree, tree[max_node][0][0])
            tree_path.append(max_node)

        tpl = max_height
        if tpl % 2 == 0:
            rst = tree_path[tpl / 2 - 1: tpl / 2 + 1]
            rst.sort()
            return rst
        else:
            return [tree_path[(tpl - 1) / 2]]

    def dfs_path(self, tree, start_node):
        """

        Arguments:
        - `self`:
        - `tree`:
        - `start_node`:
        """
        node = start_node
        rst = []
        while True:
            rst.append(node)
            if not node in tree:
                break
            node = tree[node][0][0]
        return rst[::-1]

    def dfs(self, edge_map, start_node):
        """

        Arguments:
        - `edge_map`:
        """
        handled_node = set()
        handled_node.add(start_node)
        tree = {}
        th = self.dfs_wrapper(tree, start_node,
                              edge_map, handled_node)
        return start_node, th, tree

    def dfs_wrapper(self, tree, node, edge_map, handled_node):
        """recursion dfs so we can calc the height

        return the height rooted by node

        Arguments:
        - `tree`:
        - `node`: the node to be handled
        - `edge_map`:
        - `handled_node`:
        """
        tree.setdefault(node, [])
        for sub_node in edge_map[node]:
            if sub_node in handled_node:
                continue
            handled_node.add(sub_node)
            nh = self.dfs_wrapper(tree, sub_node,
                                  edge_map, handled_node)
            tree[node].append([sub_node, nh])

        if tree[node]:
            tree[node] = sorted(tree[node], key=lambda i: -i[1])
            return tree[node][0][1] + 1
        else:
            del tree[node]
            return 1


# """
if __name__ == '__main__':
    s = Solution()
    print s.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
    print s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])


# """
