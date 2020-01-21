import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def br_find(gr, str, fns):
    visited = {str: str}
    que = deque()
    que += gr[str]

    while que:
        print(visited, que)
        usel = que.popleft()
        print(usel)
        if usel not in visited:
            visited[usel] = usel
            if usel == fns:
                print(f"We find {fns}")
                #way = str.join(way)
                return visited[usel]
            else:
                for node in gr.adj[usel]:
                    print(node)
                    if node not in visited:
                        que.append(node)
                        visited[usel] = visited[usel] + node

    return False

def gl_find(gr, str, visited):
    # if str == fns:
    #     return True
    visited[str] = True
    #print(visited)
    #print(str, gr.adj[str])
    # проход по графу
    for node in gr.adj[str]:
        if not visited[node]:  # если не посещали узел
            gl_find(gr, node, visited)

    return None


if __name__ == "__main__":
    gr = nx.Graph()
    gr.add_nodes_from("ABCDEFGHKL")
    gr.add_edges_from(
        [
            ('A', 'B'),
            ('A', 'C'),
            ('B', 'D'),
            ('D', 'K'),
            ('D', 'H'),
            ('H', 'L'),
            ('C', 'E'),
            ('E', 'G'),
            ('E', 'F')
        ]
    )
    gr.add_nodes_from("YXZ")
    gr.add_edges_from(
        [
            ("X", "Y"),
            ("Y", "Z"),
            ("Z", "X")
        ]
    )

    gr.add_nodes_from("TNPQ")
    gr.add_edges_from(
        [
            ("T", "N"),
            ("T", "P"),
            ("T", "Q")
        ]
    )

    gr.add_node("J")

    visited = {node: False for node in gr.nodes()}
    # print(br_find(gr, 'K', 'F'))
    # print(gr.edges)
    # print(gr['D'])
    # nx.draw(gr, with_labels=True)
    # plt.show()
    #print(gl_find(gr, 'A', visited))
    num = 0
    for node in gr.adj:
        if not visited[node]:  # если не посещали узел
            gl_find(gr, node, visited)
            num += 1
    print(num)

    n = 10
    adj_list = [[2, 4, 6],
                [9],
                [0, 3],
                [2, 4],
                [0, 3],
                [],
                [0, 7, 8],
                [6],
                [6],
                [1]]

    visit = [False] * n
    num_components = 0
    def dfs(v):
        visit[v] = True
        for w in adj_list[v]:
            if visit[w] == False:
                dfs(w)

    for v in range(n):
        if not visit[v]:
            dfs(v)
            num_components += 1

    print(num_components)
