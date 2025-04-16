class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = {i: [] for i in range(num_vertices)}

    def add_edge(self, v, w):
       
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"Vertex {vertex}:", " -> ".join(map(str, self.adj_list[vertex])))



if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    g.print_graph()
