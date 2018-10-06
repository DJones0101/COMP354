#!/usr/bin/env python3

# Darius Jones
# 10/2/2018
# COMP 354
# Python 3.6

import heapq as hq, networkx as nx, matplotlib.pyplot as plt, random, pylab
from collections import defaultdict


graph = {
	"a":[("b",1), ("c",6)],
	"b":[("c",7), ("d",4), ("a",1)],
	"c":[("a",6), ("b",7), ("e",3), ("d",2)],
	"d":[("b",4), ("c",2), ("e",5)],
	"e":[("d",5), ("c",3)]
}

def prims(graph):

	start = random.choice(list(graph)) 
	T = defaultdict(list)
	visited = set([start])
	edges = [(weight, start, to) for to, weight, in graph[start]]
	hq.heapify(edges)

	while edges:
		weight, frm, to = hq.heappop(edges)
		if to not in visited:
			visited.add(to)
			T[frm].append(to)
			for to_next, cost in graph[to]:
				if to_next not in visited:
					hq.heappush(edges, (weight, to, to_next))
	return T

#def kruskals():


def show_graph(graph, colorPath=False):

	G = nx.Graph()
	for frm, values in graph.items():
		for to, weight in values:
			G.add_edge(frm, to, weight=weight)

	# if colorPath:
	# 	for e in G.edges():
	# 		G[e[0]][e[1]]['color'] = 'black'
		
	# 	for i in xrange(len(p)-1):
	# 		G[p[i]][p[i+1]]['color'] = 'blue'



	
	pos = nx.circular_layout(G)
	pylab.figure(1)
	nx.draw(G,pos,with_labels=True)
	edge_labels = dict([((u,v,),d['weight'])
    for u,v,d in G.edges(data=True)])
	nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)	
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
# hhttps://stackoverflow.com/questions/34120957/python-networkx-mark-edges-by-coloring-for-graph-drawing


def main():
	show_graph(graph)
	mst = prims(graph)
	print(mst)
		



if __name__ == "__main__":
	main()