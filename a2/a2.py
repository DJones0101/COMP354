#!/usr/bin/env python3

# Darius Jones
# 10/2/2018
# COMP 354
# Python 3.6

import heapq as hq, networkx as nx, matplotlib.pyplot as plt, random, pylab
from collections import defaultdict


graph = {
	"a":[("b",1), ("c",2)],
	"b":[("c",1), ("d",4), ("a",1)],
	"c":[("a",2), ("b",1), ("e",3), ("d",2)],
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


def showGraph(graph):

	G = nx.Graph()
	for frm, values in graph.items():
		for to, weight in values:
			G.add_edge(frm, to, color='black', weight=weight)

	edges = G.edges()
	colors = [G[frm][to]['color'] for frm,to in edges]
	
	pos = nx.circular_layout(G)
	pylab.figure(1)
	nx.draw(G,pos,with_labels=True)
	nx.draw(G, pos, edges=edges, edge_color=colors, width=3)
	edge_labels = dict([((frm,to,),d['weight'])
    for frm,to,d in G.edges(data=True)])
	nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)	
	plt.draw()
	plt.show()

def showPath(graph, mst):


	path = []
	for frm, values in mst.items():
		for to in values:
			path.append((frm,to))
	print("path", path)

	G = nx.Graph()
	for frm, values in graph.items():
		for to, weight in values:
			if (frm, to) in path:
				print("green", (frm, to))		
				G.add_edge(frm, to, color='green', weight=weight)
			else:
				print("black", (frm, to))	
				G.add_edge(frm, to, color='black', weight=weight)	
				


	edges = G.edges()
	print("num of edges", len(edges))
	colors = [G[frm][to]['color'] for frm,to in edges]	
	print(colors)

	pos = nx.circular_layout(G)
	pylab.figure(1)
	nx.draw(G,pos,with_labels=True)
	edge_labels = dict([((frm,to,),d['weight'])
    for frm,to,d in G.edges(data=True)])
	nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)	
	nx.draw(G, pos, edges=edges, edge_color=colors, width=3)
	plt.draw()
	plt.show()



	

#https://stackoverflow.com/questions/29838746/how-to-draw-subgraph-using-networkx  show subgrap

# The goal is to color the edges after the algorithm was ran
# hhttps://stackoverflow.com/questions/34120957/python-networkx-mark-edges-by-coloring-for-graph-drawing


def main():
	
	mst = prims(graph)
	# showPath(graph, mst)
	showPath(graph,mst)	


	
	
		



if __name__ == "__main__":
	main()