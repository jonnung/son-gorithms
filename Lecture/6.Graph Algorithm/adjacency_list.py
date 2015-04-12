# -*- coding: utf8 -*-
"""
원본: http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
"""


class Vertex:
    """ Listing 1
    모든 간선의 가중치와 정점들간의 연결을 다룬다.

    """
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        """ 현재 정점에서 다른 정점과의 연결을 추가 """
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """ 인접리스트 안에 있는 모든 정점들을 반환 """
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        """ 현재 정점으로부터 nbr 정점까지의 가중치를 반환 """
        return self.connectedTo[nbr]


class Graph:
    """
    Listing 2
    모든 정점의 기준 리스트를 사전으로 갖고 있다.
    (Figure 4 에서 회색 박스 안에 있는 부분.)

    """
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        """ 그래프안에 모든 정점들의 이름을 반환 """
        return self.vertList.keys()

    def __iter__(self):
        """ 특정 그래프안에 있는 모든 정점들을 쉽게 iterate 하기 위함 """
        return iter(self.vertList.values())
