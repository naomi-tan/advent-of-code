import TreeUtils

# example tree
node_a = TreeUtils.Node('A')
node_b = TreeUtils.Node('B')
node_c = TreeUtils.Node('C')
node_d = TreeUtils.Node('D')
node_e = TreeUtils.Node('E')
node_f = TreeUtils.Node('F')
nodes_ls = [node_a, node_b, node_c, node_d, node_e, node_f]

#      A
#     / \
#    B   C
#   / \   \
#  D   E   F

node_a.add_child(node_b)
node_a.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)
node_c.add_child(node_f)


# breadth first search
# https://www.programiz.com/dsa/graph-bfs

def bfs():
    # A standard BFS implementation puts each vertex of the graph into one of two categories:
    #
    # Visited
    # Not Visited
    # The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.
    #
    # The algorithm works as follows:
    #
    # Start by putting any one of the graph's vertices at the back of a queue.
    # Take the front item of the queue and add it to the visited list.
    # Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the back of the queue.
    # Keep repeating steps 2 and 3 until the queue is empty.
    # The graph might have two different disconnected parts so to make sure that we cover every vertex, we can also run the BFS algorithm on every node
    visited = []
    queue = [nodes_ls[0]]

    while len(queue) != 0:
        curr_node = queue.pop()
        visited.append(curr_node)
        adj_nodes = []

        if curr_node.parent is not None:
            adj_nodes.append(curr_node.parent)
        for child_node in curr_node.children:
            adj_nodes.append(child_node)

        for node in adj_nodes:
            if visited.count(node) == 0:
                queue.insert(0, node)
    return visited

for r in bfs():
    print(r.data)



# BFS algorithm in Python
#
# import collections
#
# def bfs(graph, root):
#
#     visited, queue = set(), collections.deque([root])
#     visited.add(root)
#
#     while queue:
#
#         # Dequeue a vertex from queue
#         vertex = queue.popleft()
#         print(str(vertex) + " ", end="")
#
#         # If not visited, mark it as visited, and
#         # enqueue it
#         for neighbour in graph[vertex]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)
#
#
# if __name__ == '__main__':
#     graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
#     print("Following is Breadth First Traversal: ")
#     bfs(graph, 0)



# depth first search
# https://www.programiz.com/dsa/graph-dfs

def dfs():
    # The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.
    #
    # The DFS algorithm works as follows:
    #
    # Start by putting any one of the graph's vertices on top of a stack.
    # Take the top item off the stack and add it to the visited list.
    # Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the top of the stack.
    # Keep repeating steps 2 and 3 until the stack is empty.

    visited = []
    stack = [nodes_ls[0]]

    while len(stack) != 0:
        curr_node = stack.pop()
        visited.append(curr_node)
        adj_nodes = []

        if curr_node.parent is not None:
            adj_nodes.append(curr_node.parent)
        for child_node in curr_node.children:
            adj_nodes.append(child_node)

        for node in adj_nodes:
            if visited.count(node) == 0:
                stack.append(node)
    return visited

for r in dfs():
    print(r.data)



# DFS algorithm in Python
#
# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#
#     print(start)
#
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited
#
#
# graph = {'0': set(['1', '2']),
#          '1': set(['0', '3', '4']),
#          '2': set(['0']),
#          '3': set(['1']),
#          '4': set(['2', '3'])}
#
# dfs(graph, '0')