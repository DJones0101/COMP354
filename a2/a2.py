#!/usr/bin/env python3

# Darius Jones
# 10/2/2018
# COMP 354
# Python 3.6

import heapq as hq 
import networkx as nx 
import matplotlib.pyplot as plt
import random
from collections import defaultdict


graph = {
	"a":{"b":7, "d":5},
	"b":{"a":7, "d":9, "c":8, },
	"c":{"d":5, },
	"d":{"a":5, "b":9,},
}

def prims(graph):
	 
	T = defaultdict(set)
	start = random.choice(list(graph)) # random key from dictionary
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
	pos = nx.spring_layout(G)
	labels = nx.get_node_attributes(G,"pos")
	nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
	nx.draw(G, with_labels=True)
	plt.draw()
	plt.show()

def show_path(graph, mst):
	G = nx.Graph(graph)
	    
	pos = nx.spring_layout(G)  #setting the positions with respect to G, not k.
	k = G.subgraph(mst)  
	pos = nx.spring_layout(G)
	labels = nx.get_node_attributes(G,"pos")
	nx.draw_networkx_edge_labels(k,pos,edge_labels=labels)
	nx.draw(k, with_labels=True)
	plt.draw()
	plt.show()
	

#https://stackoverflow.com/questions/29838746/how-to-draw-subgraph-using-networkx  show subgrap

# The goal is to color the edges after the algorithm was ran
# https://stackoverflow.com/questions/25639169/networkx-change-color-width-according-to-edge-attributes-inconsistent-result


def main():

	#show_graph(graph)
	mst = prims(graph)
	#show_path(graph, mst)
	print (mst)





if __name__ == "__main__":
	main()