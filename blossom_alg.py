import networkx as nx
import pandas as pd
import time
import random

start_time = time.time()

# get samples
datasize = sum(1 for row in open('input_data.csv')) - 1 # not including header row
samplesize = datasize # 'datasize' if want to run on all orders
# random.sample returns a list of ints that will be indices to skip in skiprows
skip = sorted(random.sample(range(1, datasize+1), datasize-samplesize))
print("total:", datasize)
print("skipping:", len(skip))

data = pd.read_csv('input_data.csv', skiprows=skip)

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
matching_time = time.time() - matching_start_time

print("--- %s seconds for matching %s samples ---" % (matching_time, samplesize))
print("--- found %s matches ---" % len(matching))
# print("matchings for %s samples: %s" % (samplesize, matching))

matching_with_weights = [(node1, node2, weighted_graph[node1][node2]['weight']) for (node1, node2) in matching]
print("matchings with weights for %s samples: %s" % (samplesize, matching_with_weights))

# print("--- %s seconds for entire script ---" % (time.time() - start_time))