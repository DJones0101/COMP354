#!/usr/bin/env python3

from kmst import Vertex, Edge, kruskal


vertex1 = Vertex("a")
vertex2 = Vertex("b")
vertex3 = Vertex("c")
vertex4 = Vertex("d")
vertex5 = Vertex("e")
vertex6 = Vertex("f")

vertexList = []
vertexList.append(vertex1)
vertexList.append(vertex2)
vertexList.append(vertex3)
vertexList.append(vertex4)
vertexList.append(vertex5)
vertexList.append(vertex6)

edge1 = Edge(2, vertex1, vertex2)
edge2 = Edge(4, vertex1, vertex4)
edge3 = Edge(4, vertex2, vertex3)
edge4 = Edge(4, vertex2, vertex4)
edge5 = Edge(3, vertex2, vertex5)
edge6 = Edge(1, vertex2, vertex6)
edge7 = Edge(5, vertex3, vertex6)
edge8 = Edge(2, vertex4, vertex5)
edge9 = Edge(5, vertex5, vertex6)

edgeList = []
edgeList.append(edge1)
edgeList.append(edge2)
edgeList.append(edge3)
edgeList.append(edge4)
edgeList.append(edge5)
edgeList.append(edge6)
edgeList.append(edge7)
edgeList.append(edge8)
edgeList.append(edge9)

al = Kruskal()
al.createSpanningTree(vertexList, edgeList)