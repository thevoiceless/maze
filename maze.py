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
# Exclude unneeded vertices from final graph
vprop_include = graph.new_vertex_property("bool")

vertices = []
numVillages = 0
numVertices = 0
predList = []
path = []

# DFSVisitor class used with depth-first search
class CustomDFSVisitor(DFSVisitor):
	def __init__(self, name, predList):
		self.name = name
		self.predList = predList

	def tree_edge(self, e):
		print "Visit", vprop_label[e.target()]
		# Add vertex to path
		self.predList.append(vprop_props[e.target()])
		vprop_include[e.target()] = True
		# Stop when train line #70 is reached
		if vprop_props[e.target()][4] == 70:
			# Add the line from A to B to the start of the path
			self.predList.insert(0, vprop_props[graph.vertex(0)])
			vprop_include[graph.vertex(0)] = True
			raise StopSearch

	def finish_vertex(self, u):
		print "Finished with", vprop_label[u]
		# Pop finished vertices off of the path so that it doesn't include backtracing
		predList.pop()
		vprop_include[u] = False

def initializeFromFile(filename):
	global numVillages
	global numVertices
	global vertices

	with file(filename, "r") as f:
		# Get number of vertices and edges (not used)
		firstLine = f.readline()
		numbers = firstLine.split()
		numVillages = int(numbers[0])
		numVertices = int(numbers [1])
		# Load edge info, edges on the map are vertices in the graph
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
		# Two vertices are created for each edge from the original map
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
			# Don't connect vertices to their partner going the other direction
			if vprop_props[vSource][4] != vprop_props[vDest][4]:
				# Only connect vertices that are sequential and share at least one property
				if (vprop_props[vSource][1] == vprop_props[vDest][0]) and (vprop_props[vSource][2] == vprop_props[vDest][2] or vprop_props[vSource][3] == vprop_props[vDest][3]):
					e = graph.add_edge(vSource, vDest);

# Print the path of predecessors
def printPath():
	global predList
	print "Path: "
	for p in predList:
		print p[0],
	# Don't forget to add Village j to the end of the path
	print "j"

print "Loading vertices..."
initializeFromFile("input.txt")
print "Building graph..."
buildGraph()
print "Searching..."
dfs_search(graph, graph.vertex(0), CustomDFSVisitor(vprop_label, predList))
print "Done!"
printPath()
print "Saving graph to \'" + imageFile + "\'..."
# graph.set_vertex_filter(vprop_include);
graph_draw(graph, vertex_text=vprop_label, vertex_fill_color=vprop_color, vertex_font_size=14, edge_color=[0.179, 0.203, 0.210, 1.0], output_size=(1500, 1500), output=imageFile)
