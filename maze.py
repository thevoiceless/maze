#!/usr/bin/python

import string
from graph_tool.all import *

graph = Graph(directed = False)
vprop_label = graph.new_vertex_property("string")
eprop_color = graph.new_edge_property("string")
eprop_type = graph.new_edge_property("string")
numVillages = 0
numEdges = 0

def indexOfVertex(c):
	global graph
	# Find index of vertex with the given label
	for v in graph.vertices():
		if vprop_label[v] == c:
			return int(v)

def initializeFromFile(filename):
	global graph
	global numVillages
	global numEdges

	with file(filename, "r") as f:
		# Create list of letters A-Z, a-z
		letters = list(string.ascii_uppercase) + list(string.ascii_lowercase)
		# Get number of vertices and edges
		firstLine = f.readline()
		numbers = firstLine.split()
		numVillages = int(numbers[0])
		numEdges = int(numbers [1])
		# Add vertices with labels
		for i in range(numVillages):
			v = graph.add_vertex()
			vprop_label[graph.vertex(int(v))] = letters[i]
		# Add edges between vertices, including color and type
		for line in f:
			edgeInfo = line.split()
			e = graph.add_edge(graph.vertex(indexOfVertex(edgeInfo[0])), graph.vertex(indexOfVertex(edgeInfo[1])))
			eprop_color[e] = edgeInfo[2]
			eprop_type[e] = edgeInfo[3]
		# Create pretty picture
		graph_draw(graph, vertex_text=vprop_label, vertex_fill_color="black", vertex_font_size=18, edge_color=eprop_color, output_size=(500, 500), output="graph.png")

def DFS():
	global graph


initializeFromFile("input.txt")
tree = DFS()