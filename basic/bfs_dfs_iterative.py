graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}


def dfs(graph, root):
    seen, stack = set(), [root]
    while stack:
        vertex = stack.pop()
        if vertex not in seen:
            seen.add(vertex)
            neighbors = graph[vertex]
            unseen_neighbors = neighbors - seen
            stack.extend(unseen_neighbors)  # Extend list with set
    return seen


dfs(graph, 'A')  # {'E', 'D', 'F', 'A', 'C', 'B'}

import collections


def bfs(graph, root):
    seen, queue = set(), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        if vertex not in seen:
            seen.add(vertex)
            neighbors = graph[vertex]
            unseen_neighbors = neighbors - seen
            queue.extend(unseen_neighbors)


def visit(n):
    print(n)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2, 0], 2: []}
    bfs(graph, 0)
