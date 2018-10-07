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


def showPath(graph, mcst):
	# Colors the path of the mcst green

	path = []
	weightList = [] 
	for frm, values in mcst.items():
		for to in values:
			path.append((frm,to))

	mcstWeight = 0

	G = nx.Graph()
	for frm, values in graph.items():
		for to, weight in values:
			if (frm, to) in path:		
				weightList.append(weight)
				mcstWeight += weight
				pass
			G.add_edge(frm, to, color='black', weight=weight)

	index = 0
	for frm, to in path:
		G.add_edge(frm, to, color='green', weight=weightList[index])
		index += 1

	edges = G.edges()
	colors = [G[frm][to]['color'] for frm,to in edges]	
	pos = nx.circular_layout(G)
	nx.draw(G,pos,with_labels=True)
	edge_labels = dict([((frm,to,),d['weight'])
    for frm,to,d in G.edges(data=True)])
	nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)	
	nx.draw(G, pos, edges=edges, edge_color=colors, width=3)
	plt.draw()
	plt.show()

	print("Weight of the MCST is %d" %(mcstWeight))



def main():

	showGraph(graph)
	mcst = prims(graph)
	showPath(graph,mcst)
	



if __name__ == "__main__":
	main()