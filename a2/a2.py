#!/usr/bin/env python3

# Darius Jones
# 10/2/2018
# COMP 354
# Python 3.6


import pylab
from collections import defaultdict
#https://www.sanfoundry.com/java-program-implement-min-heap/


class heap:	
	'''
	Maintains a heap. A list must be passed to the constructor
	'''
	def __init__(self):
		self.size = 0
		self.head = 1 

		

	def parent(index):
		return (index / 2)
	
	def leftChild(index):
		return (index * 2)

	def rightChild(index):
		return (index * 2) + 1

	def isLeaf(index):

		if(index >= (self.size/2) and index <= self.size):
			return True
		else:
			return False

	def swap(src, dest):
		q[src], q[dest] = q[dest], q[src]

	def heapify(index):
		left = leftChild(index)
		right = rightChild(index)

		if isLeaf(index) == False:
			if q[index][0] > q[left][0] or q[index][0] > q[right][0]:

				if q[left][0] < q[right][0]:
					swap(index, left)
					self.heapify(left)
				else:
					swap(index, right)
					self.heapify(index, left)
	
	def insert(element):
		self.size += 1
		q.append(element)
		current = self.size

		while q[current][0] < q[parent(current)][0]:
			swap(current, parent(current))
			current = parent(current)



	def pop():
		popped = q[self.head]
		self.size -= 1
		del q[self.head]
		heapify(self.head)
		return popped
	
	def printHeap():
		print(q)




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
	"f":[("g",1)],
	"g":[("f",1)]
}

# def quickSort(array):

#     if len(array) < 2:
#         return array
#     else:
#         pivot = random.choice(array)
#         lessThanPivot = [index for index in array if index < pivot]
#         equalToPivot = [index for index in array if index == pivot]
#         greaterThanPivot = [index for index in array if index > pivot]
#         return quickSort(lessThanPivot) + equalToPivot + quickSort(greaterThanPivot)


def prims(graph):

	start = random.choice(list(graph)) 
	T = defaultdict(list)
	bookmark = set([start])
	edges = [(weight, start, to) for to, weight, in graph[start]]
	hq.heapify(edges)

	
	# the algorithm
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

	# the algorithm
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



if __name__ == "__main__":
	main()