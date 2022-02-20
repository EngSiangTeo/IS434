from flask import Flask, jsonify
from flask_cors import CORS
from flask_caching import Cache

import numpy as np
import community

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_mapping(config)
cache = Cache(app)

import networkx as nx

colours = ["red", "green", "blue", "yellow", "orange", "purple"]

def scale(x, out_range=(-1, 1)):
    domain = min(x), max(x)
    y = (x - (domain[1] + domain[0]) / 2) / (domain[1] - domain[0])
    return y * (out_range[1] - out_range[0]) + (out_range[1] + out_range[0]) / 2

def convertNodes(nodes, partition, eigenvectors, betweeness):
    degree = [int(node[1]) for node in nodes]
    size = scale(np.array(degree), (5,25))
    e_size = scale(np.array(list(eigenvectors.values())), (5,25))
    b_size = scale(np.array(list(betweeness.values())), (5,25))
    return {
            n[0] : {
                "name" : n[0],
                "degree" : n[1],
                "size" : size[index],
                "eigenvectors" : eigenvectors[n[0]],
                "e_size" : e_size[index],
                "betweeness" : betweeness[n[0]],
                "b_size" : b_size[index],
                "color" : colours[partition[n[0]]],
                "community" : partition[n[0]]
                }
                for index, n in enumerate(nodes)
            }

def convertEdges(edges):
    return {count: {"source" : edge[0], "target" : edge[1]} for count,edge in enumerate(edges)}

def convertLayout(layouts):
    return {"nodes" : {key : {"x" : layouts[key][0] * 1000, "y" : layouts[key][1] * 1000} for key in layouts}}

def prepNetwork():
    G = nx.Graph()
    edges = nx.read_edgelist('data/edges.txt')
    G.add_edges_from(edges.edges())
    partition = community.best_partition(G)
    n = convertNodes(G.degree(), partition, nx.eigenvector_centrality(G), nx.betweenness_centrality(G))
    e = convertEdges(G.edges())
    l = convertLayout(nx.spring_layout(G))
    return n,e,l, colours[:max(partition.values())+1]

@app.route("/")
@cache.cached(timeout=200)
def home():
    nodes, edges, layouts, colours = prepNetwork()
    return jsonify({
        "nodes" : nodes,
        "layouts" : layouts,
        "edges" : edges,
        "colours" : colours,
        "c_index" : [i for i in range(len(colours))]
    })


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0", debug=True)