import random
import sys


class Graph:

    def __init__(self, amount_vertices, starting_vertex):
        self.edges = {}  # dictionary of edges
        self.vertices = set()  # set of vertices
        self.amount_vertices = amount_vertices  # amount of vertices
        self.starting_vertex = starting_vertex

    def generate_random_complete_graph(self):
        for i in range(self.amount_vertices):
            for j in range(self.amount_vertices):
                if i != j:
                    weight = random.randint(1, 10)
                    print('tambah path ',i, j, weight)
                    self.add_edge(i, j, weight)

    def generate_random_complete_graph_custom(self,isian):
        print(isian)
        for i in isian:
            print([i[0], i[1], i[2]])
            self.add_edge(i[0], i[1], i[2])

    # adds a edge linking "src" in "dest" with a "cost"
    def add_edge(self, src, dest, cost=0):
        if not self.edge_exists(src, dest):
            self.edges[(src, dest)] = cost
            self.edges[(dest, src)] = cost
            self.vertices.add(src)
            self.vertices.add(dest)

    def edge_exists(self, src, dest):
        return (True if (src, dest) in self.edges else False)

    def show_graph(self):
        print('Showing the graph:\n')
        for edge in self.edges:
            print('%d linked in %d with cost %d' %
                  (edge[0], edge[1], self.edges[edge]))

    def get_cost_path(self, path):
        total_cost = 0
        for i in range(self.amount_vertices - 1):
            total_cost += self.edges[(path[i], path[i+1])]

        # add cost of the last edge
        total_cost += self.edges[(path[self.amount_vertices - 1], path[0])]
        return total_cost

    # gets random unique paths - returns a list of lists of paths
    def get_random_paths(self, max_size):
        random_paths, list_vertices = [], list(self.vertices)
        initial_vertice = self.starting_vertex

        if initial_vertice not in list_vertices:
            print('Error: initial vertice %d not exists!' % initial_vertice)
            sys.exit(1)

        list_vertices.remove(initial_vertice)
        list_vertices.insert(0, initial_vertice)

        for i in range(max_size):
            list_temp = list_vertices[1:]
            random.shuffle(list_temp)
            list_temp.insert(0, initial_vertice)

            if list_temp not in random_paths:
                random_paths.append(list_temp)

        # initial_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        # matrix_data = []

        # matrix_data.append(initial_array)

        # for _ in range(8):
        #     # Menggunakan slice [:] untuk membuat salinan array awal dan melakukan pengacakan pada salinan tersebut
        #     shuffled_array = initial_array[:]
        #     random.shuffle(shuffled_array)
            
        #     # Memastikan tidak ada hasil pengacakan yang sama sebelumnya
        #     while shuffled_array in matrix_data:
        #         random.shuffle(shuffled_array)
            
        #     # Menambahkan hasil pengacakan ke dalam array baru
        #     matrix_data.append(shuffled_array)
        matrix_data = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            ]
        # random_paths = matrix_data
        print("random path : ",random_paths)

        return random_paths
