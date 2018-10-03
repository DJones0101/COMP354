#!/usr/bin/env python3

# Darius Jones
# 10/2/2018
# COMP 354
# Python 3.6

import heapq as hq, networkx as nx, matplotlib.pyplot as plt
from collections import defaultdict


graph = {
	"a":{"b":7, "d":5},
	"b":{"a":7, "d":9, "c":8, },
	"c":{"d":5, },
	"d":{"a":5, "b":9,},
}

def prims(graph, start):
	 
	T = defaultdict(set)
	visited = set([start])
	edges = [(weight, start, to) for to, weight, in graph[start].items()]
	hq.heapify(edges)

	while edges:
		weight, frm, to = hq.heappop(edges)
		if to not in visited:
			visited.add(to)
			T[frm].add(to)
			for to_next, cost in graph[to].items():
				if to_next not in visited:
					hq.heappush(edges, (weight, to, to_next))
	return T

#def kruskals():


def show_graph(graph):

	G = nx.Graph(graph)
	pos = nx.circular_layout(G)
	labels = nx.get_node_attributes(G,"pos")
	nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
	nx.draw(G, with_labels=True)
	plt.draw()
	plt.show()


# The goal is to color the edges after the algorithm was ran
# https://stackoverflow.com/questions/25639169/networkx-change-color-width-according-to-edge-attributes-inconsistent-result


def main():

	mst = prims(graph, "a")
	show_graph(graph)
	show_graph(mst)




if __name__ == "__main__":
	main()