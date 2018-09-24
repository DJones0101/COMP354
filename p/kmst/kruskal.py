

import DisjointSet, Vertex, Edge

class Kruskal(object):
	
	def createSpanningTree(self, vertexList, edgeList):

		disjointSet = DisjointSet(vertexList)
		spanningTree = []

		edgeList.sort()

		for edge in edgeList:
			u = edge.startVertex
			v = edge.targetVeretx

			if disjointSet.find(u.parentNode) is not disjointSet.find(v.parentNode):
				spanningTree.append(edge)
				disjointSet.union(u.parentNode, v.parentNode)


		for edge in spanningTree:
			print(edge.startVertex.name, "-", edge.targetVeretx.name)





