import osmnx as ox
import networkx as nx

G = ox.graph_from_xml("../data/map.osm", True, True, True)
ox.save_graphml(G, filepath="../data/map2.graphml")
