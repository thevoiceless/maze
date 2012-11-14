#!/usr/bin/python

import string
from graph_tool.all import *

graph = Graph()
vprop_label = graph.new_vertex_property("string")
eprop_color = graph.new_vertex_property("string")
eprop_type = graph.new_vertex_property("string")
numVillages = 0
numEdges = 0

def indexOfVertex(c):
	global graph

	for v in graph.vertices():
		if vprop_label[v] == c:
			return int(v)

def initializeFromFile(filename):
	global graph
	global numVillages
	global numEdges

	with file(filename, "r") as f:
		letters = list(string.ascii_uppercase) + list(string.ascii_lowercase)
		firstLine = f.readline()
		numbers = firstLine.split()
		numVillages = int(numbers[0])
		numEdges = int(numbers [1])

		for i in range(numVillages):
			v = graph.add_vertex()
			vprop_label[graph.vertex(int(v))] = letters[i]

		#graph_draw(graph, vertex_text=vprop_label, vertex_font_size=18, output_size=(200, 200), output="g.png")
		#graph_draw(graph, vertex_text=graph.vertex_index, vertex_font_size=18, output_size=(200, 200), output="g.png")
		for line in f:
			edgeInfo = line.split()
			print edgeInfo
			e = graph.add_edge(graph.vertex(indexOfVertex(edgeInfo[0])), graph.vertex(indexOfVertex(edgeInfo[1])))

		
		graph_draw(graph, vertex_text=vprop_label, vertex_font_size=18, output_size=(500, 500), output="graph.png")
		return graph, numVillages, numEdges

graph, numVillages, numEdges = initializeFromFile("input.txt")
