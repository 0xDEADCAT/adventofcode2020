#!/usr/bin/python3
import networkx as nx
import re

input_file = "input.txt"

# Define regex rules
get_color_name = re.compile(r'^\w+ \w+(?= bags)')
get_weighted_edge = re.compile(r'(\d+) (\w+ \w+)(?= bag)')
get_weighted_edges = re.compile(r'(?<=contain )(\d+) .*( bag| bags)')

searched_node = "shiny gold"

DG = nx.DiGraph()

with open(input_file) as f:
    for line in f:
        line = line.strip()
        color = get_color_name.search(line).group(0)
        weighted_edges = get_weighted_edges.search(line)
        if weighted_edges:
            weighted_edges = weighted_edges.group(0)
            for weighted_edge in weighted_edges.split(', '):
                weighted_edge = get_weighted_edge.search(weighted_edge)
                DG.add_weighted_edges_from([(color, weighted_edge.group(2),
                                            int(weighted_edge.group(1)))])
        else:
            if not DG.has_node(color):
                DG.add_node(color)

nodes = list(DG.nodes)
nodes.remove('shiny gold')
can_contain = 0
for node in nodes:
    if nx.has_path(DG, node, searched_node):
        can_contain += 1
print(can_contain)
