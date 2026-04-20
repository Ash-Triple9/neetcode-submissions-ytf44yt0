"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        So the goal here is to create a deep copy, meaning create an entirely
        new graph based off the current one that we have.
        We are only given the head node to work with
        The nodes themselves have neighbors which act as adjacency lists, revealing the location of the other nodes.
        Our goal is to recreate the graph, with the same neighbors and values.

        So let's say the adj list looks like [[2], [1,3], [2]]
        We begin with node 1
        Node 1 will have value 1 and will have neighbor 2.
        Put 1 down as visited
        Then we move to node 2
        Value 2, neighbors 1, 3
        Put 2 down as visited
            But we already visited 1, so we don't visit it again
            We go to node 3
        Value 3, neighbors 2
        Put 3 down as visited

        Deep copy part:
        Enqueue the original node itself 
        While queue
            pop the current node and enqueue its neighbors if they are not visited yet
            mark it as visited
            For the current node,
                Make a new node and transfer the values as well as the neighboring values into that new node
                Neighboring nodes need not be visited or unvisited
        '''
        if not node:
            return node
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)


        

        