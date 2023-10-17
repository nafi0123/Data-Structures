graph={ }
flag = True
total_vertex = int(input("Enter no. of vertex: "))
visited=[]
stack=[]
def dfs(graph,temp):#function for dfs
    stack.append(temp)
    visited.append(temp)
    while stack:
        node=stack.pop()
        print(node,end=" ")
        for child in graph[node]:
            if child not in visited:
                stack.append(child)
                visited.append(child)

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
dfs(graph,'A')
