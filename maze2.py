#!/usr/bin/python

import string
from graph_tool.all import *

# Filename for the final graph
imageFile = "graph.png"
# Vertext properties
graph = Graph()
vprop_label = graph.new_vertex_property("string")
vprop_color = graph.new_vertex_property("string")
vprop_type = graph.new_vertex_property("string")
vprop_props = graph.new_vertex_property("object")
# Eclude unneeded vertices and endges from final graph
vprop_include = graph.new_vertex_property("bool")
eprop_include = graph.new_edge_property("bool")

vertices = []
numVillages = 0
numVertices = 0
pred = []
path = []

# DFSVisitor class used with depth-first search
class CustomDFSVisitor(DFSVisitor):
	def __init__(self, name, pred):
		self.name = name
		self.pred = pred
		self.end = False

	def discover_vertex(self, u):
		print "--> Traverse", self.name[u]
		self.pred.append(u)
		vprop_include[u] = True

	def examine_edge(self, e):
		eprop_include[e] = True

	def finish_vertex(self, u):
		# self.pred.append(u)
		if vprop_props[u][4] == 70:
			raise StopSearch

def initializeFromFile(filename):
	global numVillages
	global numVertices
	global vertices

	with file(filename, "r") as f:
		# Get number of vertices and edges
		firstLine = f.readline()
		numbers = firstLine.split()
		numVillages = int(numbers[0])
		numVertices = int(numbers [1])
		# Load edge info, edges will become vertices
		vertices = []
		i = 0
		for line in f:
			props = line.split()
			vertices.append(props)
			i += 1

def buildGraph():
	global graph
	# Add vertices with labels
	i = 0
	for vert in vertices:
		i += 1
		vert.append(i)
		# Two vertices for each edge from the original map
		# One for traversing the edge in alphabetical order
		v = graph.add_vertex()
		vprop_label[graph.vertex(int(v))] = (str(i) + vert[0] + vert[1])
		vprop_color[graph.vertex(int(v))] = vert[2]
		vprop_type[graph.vertex(int(v))] = vert[3]
		vprop_props[graph.vertex(int(v))] = vert
		vprop_include[graph.vertex(int(v))] = False
		count = 0
		# And one for the opposite direction
		v = graph.add_vertex()
		vprop_label[graph.vertex(int(v))] = (str(i) + vert[1] + vert[0])
		vprop_color[graph.vertex(int(v))] = vert[2]
		vprop_type[graph.vertex(int(v))] = vert[3]
		reverseDir = []
		reverseDir.append(vert[1])
		reverseDir.append(vert[0])
		reverseDir.append(vert[2])
		reverseDir.append(vert[3])
		reverseDir.append(vert[4])
		vprop_props[graph.vertex(int(v))] = reverseDir
		vprop_include[graph.vertex(int(v))] = False

	# Connect vertices
	for vSource in graph.vertices():
		for vDest in graph.vertices():
			if vprop_props[vSource][4] != vprop_props[vDest][4]:
				if (vprop_props[vSource][1] == vprop_props[vDest][0]) and (vprop_props[vSource][2] == vprop_props[vDest][2] or vprop_props[vSource][3] == vprop_props[vDest][3]):
					# print "Edge between", vprop_props[vSource], "and", vprop_props[vDest]
					e = graph.add_edge(vSource, vDest);
					eprop_include[e] = False
		# print vprop_props[vSource]

# Print the path of predecessors
def printPath():
	global pred
	prev = ""
	for p in pred:
		print vprop_label[graph.vertex(p)]
		# village = vprop_props[graph.vertex(p)][0]
		# if prev != village:
		# 	path.append(village)
		# prev = village
	path.append('j')
	print "Path:",
	for village in path:
		print village,
	print

print "Loading vertices..."
initializeFromFile("input.txt")
print "Building graph..."
buildGraph()
print "Searching..."
dfs_search(graph, graph.vertex(0), CustomDFSVisitor(vprop_label, pred))
print "Done!"
printPath()
print "Saving graph to \'" + imageFile + "\'..."
# graph.set_edge_filter(eprop_include)
# graph.set_vertex_filter(vprop_include);
graph_draw(graph, vertex_text=vprop_label, vertex_fill_color=vprop_color, vertex_font_size=14, edge_color=[0.179, 0.203, 0.210, 1.0], output_size=(1500, 1500), output=imageFile)
