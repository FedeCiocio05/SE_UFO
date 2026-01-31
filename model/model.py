from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.lista_anni = []
        self.lista_shapes = []
        self._nodes = []
        self._edges = []
        self.id_map = {}

    def load_anni(self):
        self.lista_anni = DAO.get_anno()
        return self.lista_anni

    def load_shape(self, anno):
        self.lista_shapes = DAO.get_shape(anno)
        return self.lista_shapes

    def build_graph(self, anno, shape):
        """Creazione grafo"""
        self.G.clear()

        # nodi
        self._nodes = DAO.get_nodes_stati()
        self.G.add_nodes_from(self._nodes)

        # mappa {id --> oggetto }
        for n in self._nodes:
            self.id_map[n.id] = n

        #archi
        archi = DAO.get_edges(anno, shape)
        for s1,s2,peso in archi:
            n1 = self.id_map[s1]
            n2 = self.id_map[s2]
            self.G.add_edge(n1, n2, weight=peso)

        print(f'Nodi: {self.G.number_of_nodes()}, archi: {self.G.number_of_edges()}')
        return self.G

    def get_graph_details(self):
        return self.G.number_of_nodes(), self.G.number_of_edges()

    def vicini(self):
        result = []
        for stato in self.G.nodes():
            somma = 0
            for vicino in self.G.neighbors(stato):
                w = self.G[stato][vicino]['weight']
                somma += w
            result.append((stato,somma))
        return result