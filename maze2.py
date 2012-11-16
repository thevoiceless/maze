#!/usr/bin/python

import string
from graph_tool.all import *

graph = Graph()
vprop_label = graph.new_vertex_property("string")
vprop_color = graph.new_vertex_property("string")
vprop_type = graph.new_vertex_property("string")
vprop_parent = graph.new_vertex_property("object")
vertices = []
numVillages = 0
numVertices = 0

def indexOfVertex(c):
	global graph
	# Find index of vertex with the given label
	for v in graph.vertices():
		if vprop_label[v] == c:
			return int(v)

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
			i = i + 1

def buildGraph():
	global graph
	# Add vertices with labels
	i = 0
	for vert in vertices:
		i = i + 1
		# Two vertices for each edge from the original map, one for traversing the edge in each direction
		v = graph.add_vertex()
		vprop_label[graph.vertex(int(v))] = (str(i) + vert[0] + vert[1])
		vprop_color[graph.vertex(int(v))] = vert[2];
		vprop_type[graph.vertex(int(v))] = vert[3];
		v = graph.add_vertex()
		vprop_label[graph.vertex(int(v))] = (str(i) + vert[1] + vert[0])
		vprop_color[graph.vertex(int(v))] = vert[2];
		vprop_type[graph.vertex(int(v))] = vert[3];

print "Loading vertices..."
initializeFromFile("input.txt")
buildGraph()
print "Drawing..."
graph_draw(graph, vertex_text=vprop_label, vertex_fill_color=vprop_color, vertex_font_size=14, output_size=(900, 900), output="graph.png")