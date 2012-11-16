#!/usr/bin/python

import string
from graph_tool.all import *

graph = Graph()
vprop_label = graph.new_vertex_property("string")
vprop_color = graph.new_vertex_property("string")
vprop_type = graph.new_vertex_property("string")
vprop_props = graph.new_vertex_property("object")
vertices = []
numVillages = 0
numVertices = 0

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
		# Two vertices for each edge from the original map, one for traversing the edge in each direction
		v = graph.add_vertex()
		vprop_label[graph.vertex(int(v))] = (str(i) + vert[0] + vert[1])
		vprop_color[graph.vertex(int(v))] = vert[2]
		vprop_type[graph.vertex(int(v))] = vert[3]
		vprop_props[graph.vertex(int(v))] = vert
		count = 0
		
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

	for vSource in graph.vertices():
		for vDest in graph.vertices():
			if vprop_props[vSource][4] != vprop_props[vDest][4]:
				if (vprop_props[vSource][1] == vprop_props[vDest][0]) and (vprop_props[vSource][2] == vprop_props[vDest][2] or vprop_props[vSource][3] == vprop_props[vDest][3]):
					print "Link", vprop_label[vSource], "and", vprop_label[vDest]
					graph.add_edge(vSource, vDest);
		# print vprop_label[vSource], vprop_props[vSource]
		


print "Loading vertices..."
initializeFromFile("input.txt")
buildGraph()
print "Drawing..."
graph_draw(graph, vertex_text=vprop_label, vertex_fill_color=vprop_color, vertex_font_size=14, output_size=(1000, 1000), output="graph.png")