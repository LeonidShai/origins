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
    print(br_find(gr, 'K', 'F'))
    # print(gr.edges)
    # print(gr['D'])
    # nx.draw(gr, with_labels=True)
    # plt.show()
