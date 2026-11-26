class Grafo:
    def __init__(self):
        # Diccionario para guardar cada nodo y sus vecinos conectados
        self.adyacencia = {}

    def mostrar_grafo(self):
        print("Estado actual del grafo:")
        for nodo, vecinos in self.adyacencia.items():
            print(f"  {nodo} -> {vecinos}")

if __name__ == "__main__":
    g = Grafo()
    g.mostrar_grafo()
