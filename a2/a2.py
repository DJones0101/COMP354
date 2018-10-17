#!/usr/bin/env python3

# Darius Jones
# Chad Bloor
# Gerardo Carillo
# 10/16/2018
# COMP 354
# Python 3.6

import pdb
import networkx as nx 
import matplotlib.pyplot as plt 
import random 
import pylab
from collections import defaultdict


class HeapQ(object):

    def __init__(self):
        self.items = [0]

    def __len__(self):
        return len(self.items) - 1

    def size(self):
    	return len(self.items) - 1

    def floatUp(self):
        index = len(self)
        while index  // 2 > 0:
            if self.items[index] < self.items[index  // 2]:
                self.swap(index // 2, index)
            index  = index  // 2

    def pushElement(self, element):
        self.items.append(element)
        self.floatUp()

    def swap(self, index1, index2):
    	self.items[index1], self.items[index2] = self.items[index2], self.items[index1]


    def sinkDown(self, index):
        while index * 2 <= len(self):
            minChild = self.minChild(index)
            if self.items[index] > self.items[minChild]:
                self.swap(index,minChild)
            index = minChild

    def minChild(self, index):
        if index * 2 + 1 > len(self):
            return index * 2

        if self.items[index * 2] < self.items[index * 2 + 1]:
            return index * 2
        return index * 2 + 1

    def popElement(self):
    	retVal = self.items[1]
    	self.items[1] = self.items[len(self)]
    	self.items.pop()
    	self.sinkDown(1)
    	return retVal

    def printHeap(self):
    	print(self.items[1:])


graph = {
	"a":[("b",1), ("c",2)],
	"b":[("c",1), ("d",4), ("a",1)],
	"c":[("a",2), ("b",1), ("e",3), ("d",2)],
	"d":[("b",4), ("c",2), ("e",5)],
	"e":[("d",5), ("c",3)]
}

graph1 = {
	"a":[("b",1), ("c",2)],
	"b":[("c",1), ("d",4), ("a",1)],
	"c":[("a",2), ("b",1), ("e",3), ("d",2)],
	"d":[("b",4), ("c",2), ("e",5)],
	"e":[("d",5), ("c",3)],
	"f":[("g", 1),("h",5)],
	"g":[("f",1),("h",2)],
	"h":[("f",5),("g",2)]
}



def prims(graph):

	start = random.choice(list(graph)) 
	edges = [(weight, start, to) for to, weight, in graph[start]]
	h = HeapQ()
	for weight, frm, to in edges:
		h.pushElement((weight, frm, to))

	#the algorithm
	T = defaultdict(list)
	bookmark = [start]

	while h.size() > 0 :
		#h.printHeap()
		#pdb.set_trace() 
		weight, frm, to = h.popElement()
		if to not in bookmark:
			bookmark.append(to)
			T[frm].append(to)
			for to_next, cost in graph[to]:
				if to_next not in bookmark:
					#print("to = %s, to_next = %s, weight = %d  " %(to,to_next, cost))
					h.pushElement((cost, to, to_next))

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
			bookmark.append(to)
			T[frm].append(to)
			#print(T)
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


	showGraph(graph1)


	Pmcst = prims(graph1)
	showPath(graph1, Pmcst)
	for frm, values in Pmcst.items():
		for to in values:
			print("%s --> %s" %(frm,to))


	Kmcst = kruskals(graph1)
	showPath(graph1, Kmcst)
	for frm, values in Kmcst.items():
		for to in values:
			print("%s --> %s" %(frm,to))


	print("-" * 50)

	showGraph(graph)


	Pmcst = prims(graph)
	showPath(graph, Pmcst)

	for frm, values in Pmcst.items():
		for to in values:
			print("%s --> %s" %(frm,to))



if __name__ == "__main__":
	main()