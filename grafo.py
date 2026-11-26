class Grafo:
    def __init__(self, dirigido=False):
        self.adyacencia = {}
        self.dirigido = dirigido

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = []

    def agregar_arista(self, origen, destino):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        if destino not in self.adyacencia[origen]:
            self.adyacencia[origen].append(destino)
        if not self.dirigido and origen not in self.adyacencia[destino]:
            self.adyacencia[destino].append(origen)

    def eliminar_arista(self, origen, destino):
        if origen in self.adyacencia and destino in self.adyacencia[origen]:
            self.adyacencia[origen].remove(destino)
        if not self.dirigido and destino in self.adyacencia and origen in self.adyacencia[destino]:
            self.adyacencia[destino].remove(origen)

    def eliminar_vertice(self, vertice):
        if vertice in self.adyacencia:
            del self.adyacencia[vertice]
            for vecinos in self.adyacencia.values():
                if vertice in vecinos:
                    vecinos.remove(vertice)

    def mostrar_grafo(self):
        print("Estado actual del grafo:")
        for nodo, vecinos in self.adyacencia.items():
            print(f"  {nodo} -> {vecinos}")

if __name__ == "__main__":
    g = Grafo()
    g.agregar_arista("A", "B")
    g.agregar_arista("A", "C")
    g.agregar_arista("B", "D")
    g.mostrar_grafo()
    print("\nEliminando arista A - C y vértice D...")
    g.eliminar_arista("A", "C")
    g.eliminar_vertice("D")
    g.mostrar_grafo()
