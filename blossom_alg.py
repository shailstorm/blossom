import networkx as nx
import pandas as pd
import time

start_time = time.time()

data = pd.read_csv('data.csv')

# create empty graph
weighted_graph = nx.Graph()

# add all nodes and weighted edges to graph
for i, row in data.iterrows():
    order1 = row['order1']
    order2 = row['order2']
    totalshared = row['totalshared']

    if not weighted_graph.has_node(order1):
        weighted_graph.add_node(order1)
    if not weighted_graph.has_node(order2):
        weighted_graph.add_node(order2)
    weighted_graph.add_edge(order1, order2, weight=totalshared)

# 'matching' is a set of tuples of each optimal match
matching_start_time = time.time()
matching = nx.max_weight_matching(weighted_graph, maxcardinality=True)
print("--- %s seconds for matching ---" % (time.time() - matching_start_time))

print("MATCHING:", matching)


print("--- %s seconds for entire script ---" % (time.time() - start_time))
