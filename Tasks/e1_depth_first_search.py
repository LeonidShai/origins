from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
	"""
	Do an depth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node of search
	:return: list of nodes in the visited order
	"""
	print(g, start_node)
	return list(g.nodes)

def dfs_find(graph, src, dst, visited):
	# наш поиск в глубину
	# src - откуда ищем
	# dst - узел, который ищем

	if src == dst:
		return True
	visited[src] = True
	# проход по графу
	for node in graph.adj:
		if not visited[node]:  # если не посещали узел
			if dfs_find(graph, node, dst, visited):
				return True

	return False

def new_dfs_find(graph, src, dst, visited):
	# функция поиска количества связанностей в графе
	posetil = []
	if src == dst:
		print(posetil)
		return True
	visited[src] = True
	# проход по графу
	for node in graph.adj:
		print(node)
		if not visited[node]:  # если не посещали узел
			if dfs_find(graph, node, dst, visited):
				return True

	return False


if __name__ == "__main__":
	graph = nx.Graph()
	graph.add_nodes_from("ABCDEFG")  # узлы графа
	graph.add_edges_from(
		[
			("A", "B"),
			("A", "C"),
			("B", "D"),
			("B", "E"),
			("C", "F"),
			("E", "G")
		]
	)  # рёбра графа

	graph.add_nodes_from("YXZ")
	graph.add_edges_from(
		[
			("X", "Y"),
			("Y", "Z"),
			("Z", "X")
		]
	)
	src = "A"
	dst = "G"
	visited = {node: False for node in graph.nodes()}  # узлы, в которых были
	# print(graph.nodes())
	# print(graph.edges())
	# print(graph.adj)
	# матрица смежности н-графа:
	# for node in graph.adj:
	# 	print(node, graph.adj[node])
	print(new_dfs_find(graph, src, dst, visited))