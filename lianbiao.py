class Ver_tex:
    def __init__(self, data):
        self.data = data
        self.firstEdge = None


class Edge:
    def __init__(self, adj_Vex, weight):
        self.adj_Vex = adj_Vex
        self.weight = weight
        self.nextEdge = None


class VexList:
    def __init__(self, vertex):
        self.listVex = []
        for i in range(len(vertex)):
            self.listVex.append(Ver_tex(i))

    def getPotion(self, v):
        for i in range(len(self.listVex)):
            if self.listVex[i].data == v:
                return i
        return -1

    def inEdge(self, e):
        index = self.getPotion(e[0])
        newEdge = Edge(self.getPotion(e[1]), e[2])
        p = self.listVex[index].firstEdge
        if p is None:
            p.firstEdge = newEdge
        else:
            while p.nextEdge is not None:
                p = p.nextEdge
            p.nextEdge = newEdge
