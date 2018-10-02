#!/usr/bin/env python3

# Darius Jones
# 10/2/2018
# COMP 354
# Python 3.6

import heapq as hq
import itertools 
import networkx as nx
import matplotlib.pyplot as plt
from dataclasses import dataclass, field
from typing import Any
q = []
entry_finder = {}
REMOVED = "<REMOVED_TASK>"
counter = itertools.count()


def add_task(task, priority=0):
	if task in entry_finder:
		remove_task(task)
		count = next(counter)
		entry = [priority, count, task]
		entry_finder[task] = entry
		hq.heappush(q, entry)

def remove_task(task):
	entry = entry_finder.pop(task)
	entry[-1] = REMOVED

def pop_task():
	while q:
		priority, count, task = hq.heappop(q)
		if task is not REMOVED:
			del entry_finder[task]
			return task
	raise KeyError("Pop from empty priority queue.") 

def prims():
def kruskals():

def main():

	G = nx.Graph()
	G.add_node("A")
	G.add_node("B")
	G.add_node("C")
	G.add_node("D")
	G.add_node("E")

	G.add_edge("A","B", weight= 1.0)
	G.add_edge("B","C", weight= 5.0)
	G.add_edge("C","A", weight= 7.0)
	G.add_edge("A","D", weight= 3.0)
	G.add_edge("D","E", weight= 6.0)
	G.add_edge("E","C", weight= 4.0)
	G.add_edge("C","D", weight= 2.0)
	pos = nx.spectral_layout(G)
	labels = nx.get_edge_attributes(G,'weight')
	nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
	
	nx.draw_spectral(G, with_labels=True)
	plt.draw()
	plt.show()



if __name__ == "__main__":
	main()