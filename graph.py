from copy import deepcopy

class Graph:
    def __init__(self, n, p):
        self.g = {}
        self.kernel = []
        # Je cree le graph en decroissant (de n a 1)
        for i in range(n, 0, -1):
            self.g[i] = list(range(max(1, i - p), i))
        self.build_kernel()

    def build_kernel(self):
        current_graph = deepcopy(self.g)

        while len(current_graph) > 0:
            # Je trouve les culs de sac
            deadend = []
            for summit in current_graph:
                if len(current_graph[summit]) == 0:
                    deadend.append(summit)
            # Je trouve les predecesseurs des culs de sacs
            prev = []
            for summit in current_graph:
                if len(set(deadend).intersection(set(current_graph[summit]))) > 0:
                    prev.append(summit)
            # J'ajoute les culs de sacs au noyau
            self.kernel.extend(deadend)
            # Les supprimer du graphe courant
            to_delete = deadend + prev
            for summit in current_graph:
                current_graph[summit] = list(set(current_graph[summit]).difference(set(to_delete)))
            # Supp les occurences das les cles
            for summit in to_delete:
                del current_graph[summit]
