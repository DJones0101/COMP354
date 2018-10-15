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
#https://www.sanfoundry.com/java-program-implement-min-heap/


class HeapQ(object):

    def __init__(self):
        self.items = [0]

    def __len__(self):
        return len(self.items) - 1

    def size(self):
    	return len(self.items) - 1

    def floatUP(self):
        i = len(self)
        while i // 2 > 0:
            if self.items[i] < self.items[i // 2]:
                self.items[i // 2], self.items[i] = \
                    self.items[i], self.items[i // 2]
            i = i // 2

    def pushElement(self, k):
        self.items.append(k)
        self.floatUP()

    def sinkDown(self, i):
        while i * 2 <= len(self):
            mc = self.minChild(i)
            if self.items[i] > self.items[mc]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > len(self):
            return i * 2

        if self.items[i * 2] < self.items[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def popElement(self):
    	return_value = self.items[1]
    	self.items[1] = self.items[len(self)]
    	self.items.pop()
    	self.sinkDown(1)
    	return return_value

    def heapify(self, listn):
    	i = len(listn) // 2
    	self.items = [0] + listn
    	while i > 0:
    		self.sinkDown(i)
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
	edges = [(weight, start, to) for to, weight, in graph[start]]
	h = HeapQ()
	for weight, frm, to in edges:
		h.pushElement((weight, frm, to))

	#the algorithm
	T = defaultdict(list)
	bookmark = [start]

	while h.size() > 0 :
		#pdb.set_trace() 
		weight, frm, to = h.popElement()
		if to not in bookmark:
			bookmark.append(to)
			T[frm].append(to)
			for to_next, cost in graph[to]:
				if to_next not in bookmark:
					h.pushElement((weight, to, to_next))

	return T



def kruskals(graph):

	T = defaultdict(list)
	edges = []
	for frm, values in graph.items():
		for to, weight in values:
			edges.append((weight,frm,to))

	edges = sorted(edges)

	#The algorithm 
	start = edges[0][1]
	bookmark = [start]
	
	for weight, frm, to in edges:
		if to not in bookmark:
			bookmark.append(to)
			T[frm].append(to)
	return T

def main():

	gList = []

	hq = heap()
	for frm, values in graph.items():
		for to, weight in values:
			gList.append((weight, frm, to))
	# for i in gList:
	# 	hq.insert(gList[i])
	for i in range(len(gList)):
		print(gList[i][0])



	# showGraph(graph)
	# Kmcst = kruskals(graphNoncon)
	# Pmcst = prims(graphNoncon)

	# cost1 = showPath(graph,Kmcst)
	# cost2 = showPath(graph,Pmcst)

	# print("Kruskal's  cost is %d " %(cost1))
	# for frm, values in Kmcst.items():
	# 	for to in values:
	# 		print("%s ---> %s" %(frm, to))

	# print("Prims's cost is %d " %(cost2))
	# for frm, values in Pmcst.items():
	# 	for to in values:
	# 		print("%s ---> %s" %(frm, to))
	pass


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