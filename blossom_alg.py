import networkx as nx
import pandas as pd
import time
import random

start_time = time.time()

# get samples
totalrows = sum(1 for row in open('input_data.csv')) - 1 # not including header row
samplesize = 1000
# random.sample returns a list of ints that will be indices to skip in skiprows
skip = sorted(random.sample(range(1, totalrows+1), totalrows-samplesize))
print("total:", totalrows)
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
print("matchings for %s samples: %s" % (samplesize, matching))


print("--- %s seconds for entire script ---" % (time.time() - start_time))