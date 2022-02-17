from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

import networkx as nx

def convertNodes(nodes):
    return {n : {"name" : n} for n in nodes}

def convertEdges(edges):
    return {count: {"source" : edge[0], "target" : edge[1]} for count,edge in enumerate(edges)}

def convertLayout(layouts):
    return {"nodes" : {key : {"x" : layouts[key][0] * 1000, "y" : layouts[key][1] * 1000} for key in layouts}}

def prepNetwork():
    G = nx.Graph()
    edges = nx.read_edgelist('data/edges.txt')
    G.add_edges_from(edges.edges())
    n = convertNodes(G.nodes())
    e = convertEdges(G.edges())
    l = convertLayout(nx.spring_layout(G))
    return n,e,l

@app.route("/")
def home():
    nodes, edges, layouts = prepNetwork()
    return jsonify({
        "nodes" : nodes,
        "layouts" : layouts,
        "edges" : edges
    })


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0", debug=True)