import osmnx as ox
import networkx as nx

G = ox.graph_from_xml("../data/map.osm", False, True, True)
ox.plot_graph(G)
ox.save_graphml(G, filepath="../data/map3.graphml")
