#-------------------
# Author: CS Inside
#-------------------
queue = []
visited = []
graph = {}
flag = True

def BFS(graph, tmp):
    queue.append(tmp)
    visited.append(tmp)

    while queue:
        node = queue.pop(0)
        print(node, end=' ')

        for child in graph[node]:
            if child not in visited:
                queue.append(child)
                visited.append(child)

def DFS(graph, tmp):
    stack.append(tmp)
    visited.append(tmp)

    while stack:
        node = stack.pop()
        print(node, end=' ')

        for child in graph[node]:
            if child not in visited:
                stack.append(child)
                visited.append(child)


total_vertex = int(input("Enter no. of vertex: "))

for i in range(total_vertex):
    vertex = input("Enter vertex: ")
    graph[vertex] = list()
    while flag:
        child = input(f'Enter child of {vertex} (-1 for exit): ')
        if child != '-1':
            graph[vertex].append(child)
        else:
            flag = False
    flag = True

print(graph)
BFS(graph, 'A')
visited.clear()
print()
DFS(graph, 'A')
