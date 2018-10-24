#!/usr/bin/env python3

# Darius Jones
# 10/2018
# Kruskal's Algorithm

import networkx as nx 
import matplotlib.pyplot as plt 
import random 
import pylab
from collections import defaultdict

graph = {
	"a":[("b",1), ("c",2)],
	"b":[("c",1), ("d",4), ("a",1)],
	"c":[("a",2), ("b",1), ("e",3), ("d",2)],
	"d":[("b",4), ("c",2), ("e",5)],
	"e":[("d",5), ("c",3)]
}


def createGraph(input):
	# takes a input file, adjacency matrix for a file and turns it into a dictionary
	# needs work 
	with open('input.txt', 'r') as file:
    	columns = next(f).split()
    	graph = defaultdict(list)
    	for line in file:
        	items = line.split()
        	row, vals = items[0], items[1:]
        	for col, val in zip(columns, vals):
            	matrix[col].append(int(val))
return graph

def kruskals(graph):

	edges = []
	for frm, values in graph.items():
		for to, weight in values:
			edges.append((weight,frm,to))
	edges = sorted(edges)
	#edges = edges[::-1]  #reversing to non-increasing makes it a Max Cost Spanning Tree

	start = edges[0][1]
	bookmark = [start]

	#the algorithm
	T = defaultdict(list)
	for weight, frm, to in edges:
		if to not in bookmark:
			bookmark.append(to)
			T[frm].append(to)
	return T


def showGraph(graph, mcst=None):
	
	if mcst != None:
		path = []
		for frm, values in mcst.items():
			for to in values:
				path.append((frm,to))

	G = nx.Graph()
	for frm, values in graph.items():
		for to, weight in values:
			G.add_edge(frm, to, color='black', weight=weight)

	if mcst != None:	
		for frm, to in path:
			G.add_edge(frm, to, color='green')

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


def main():
	showGraph(graph)
	mcst = kruskals(graph)
	for frm, listn in mcst.items():
		for to in listn:
			print("%s ---> %s" %(frm,to))
	showGraph(graph,mcst)



if __name__ == "__main__":
	main()