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


graphNoncon = {
	"a":[("b",1), ("c",2)],
	"b":[("c",1), ("d",4), ("a",1)],
	"c":[("a",2), ("b",1), ("e",3), ("d",2)],
	"d":[("b",4), ("c",2), ("e",5)],
	"e":[("d",5), ("c",3)],
	"f":[("g",-1)],
	"g":[("f",-1)]
}


def prims(graph):

	start = random.choice(list(graph)) 
	T = defaultdict(list)
	bookmark = set([start])
	edges = [(weight, start, to) for to, weight, in graph[start]]
	hq.heapify(edges)

	while edges:
		weight, frm, to = hq.heappop(edges)
		if to not in bookmark:
			bookmark.add(to)
			T[frm].append(to)
			for to_next, cost in graph[to]:
				if to_next not in bookmark:
					hq.heappush(edges, (weight, to, to_next))
	return T



def kruskals(graph):

	T = defaultdict(list)
	edges = []
	for frm, values in graph.items():
		for to, weight in values:
			edges.append((weight,frm,to))

	edges = sorted(edges)
	start = edges[0][1]
	bookmark = [start]

	for weight, frm, to in edges:
		if to not in bookmark:
			bookmark.append( to)
			T[frm].append(to)
	return T


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
	for frm, values in mcst.items():
		for to in values:
			path.append((frm,to))

	mcstWeight = 0
	weightList = []

	G = nx.Graph()
	for frm, values in graph.items():
		for to, weight in values:
			if (frm, to) in path:		
				mcstWeight += weight
				weightList.append(weight)
			G.add_edge(frm, to, color='black', weight=weight)



	for frm, to in path:
		G.add_edge(frm, to, color='green')
		

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

	return mcstWeight



def main():



	showGraph(graph)
	Kmcst = kruskals(graph)
	Pmcst = prims(graph)

	cost1 = showPath(graph,Kmcst)
	cost2 = showPath(graph,Pmcst)

	print("Kruskal's  cost is %d " %(cost1))
	for frm, values in Kmcst.items():
		for to in values:
			print("%s ---> %s" %(frm, to))

	print("Prims's cost is %d " %(cost2))
	for frm, values in Pmcst.items():
		for to in values:
			print("%s ---> %s" %(frm, to))

	


if __name__ == "__main__":
	main()