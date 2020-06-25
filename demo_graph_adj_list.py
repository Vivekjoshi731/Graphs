class Vertex:
	def __init__(self, n):
		self.name = n
		self.adjacent = list()
	
	def add_adjacent(self, v, weight):
		if v not in self.adjacent:
			self.adjacent.append((v, weight))
			self.adjacent.sort()

class Graph:
	vertices = {}
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v, weight=0):
		if u in self.vertices and v in self.vertices:
			self.vertices[u].add_adjacent(v, weight)
			self.vertices[v].add_adjacent(u, weight)
			return True
		else:
			return False
			
	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].adjacent))

g = Graph()

g.add_vertex(Vertex('A'))
g.add_vertex(Vertex('B'))
g.add_vertex(Vertex('C'))
g.add_vertex(Vertex('D'))
g.add_vertex(Vertex('E'))
g.add_vertex(Vertex('F'))


edges = ['AB', 'AE', 'AC', 'BD', 'DE', 'EF', 'CF', 'BC']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])

g.print_graph()