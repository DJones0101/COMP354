#!/usr/bin/env python3

# Darius Jones
# 10/2/2018
# COMP 354
# Python 3.6

import pdb
import networkx as nx 
import matplotlib.pyplot as plt 
import random 
import pylab
from collections import defaultdict


class BinaryHeap(object):
    def __init__(self):
        self.items = [0]

    def __len__(self):
        return len(self.items) - 1
    def size(self):
    	return len(self.items) - 1

    def percolate_up(self):
        i = len(self)
        while i // 2 > 0:
            if self.items[i] < self.items[i // 2]:
                self.items[i // 2], self.items[i] = \
                    self.items[i], self.items[i // 2]
            i = i // 2

    def insert(self, k):
        self.items.append(k)
        self.percolate_up()

    def percolate_down(self, i):
        while i * 2 <= len(self):
            mc = self.min_child(i)
            if self.items[i] > self.items[mc]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > len(self):
            return i * 2

        if self.items[i * 2] < self.items[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def del_min(self):
    	return_value = self.items[1]
    	self.items[1] = self.items[len(self)]
    	self.items.pop()
    	self.percolate_down(1)
    	return return_value

    def build_heap(self, alist):
    	i = len(alist) // 2
    	self.items = [0] + alist
    	while i > 0:
    		self.percolate_down(i)
    		i -= 1


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
	bookmark = ([start])
	edges = [(weight, start, to) for to, weight, in graph[start]]
	h = BinaryHeap()
	for weight, frm, to in edges:
		h.insert((weight, frm, to))

	#the algorithm
	while h.size() > 0 :
		#pdb.set_trace()
		weight, frm, to = h.del_min()

		if to not in bookmark:
			bookmark.append(to)
			T[frm].append(to)
			for to_next, cost in graph[to]:
				if to_next not in bookmark:
					h.insert((weight, to, to_next))

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

	#The algorithm 
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

	Pmcst = prims(graph)
	showPath(graph, Pmcst)

	for frm, values in Pmcst.items():
		for to in values:
			print("%s --> %s" %(frm,to))



if __name__ == "__main__":
	main()