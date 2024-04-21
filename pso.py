import matplotlib.pyplot as plt

from gui.g_main import *
from pso.pso_main import *

if __name__ == "__main__":

    # inisial sesuai jurnal
    initial_path = [
        [0, 1, 3] ,
        [0, 2, 0] ,
        [0, 3, 5] ,
        [0, 4, 0] ,
        [0, 5, 0] ,
        [0, 6, 0] ,
        [0, 7, 0] ,
        [0, 8, 0] ,
        [0, 9, 0] ,
        [0, 10, 0] ,
        [0, 11, 0] ,
        [1, 0, 3] ,
        [1, 2, 0] ,
        [1, 3, 0] ,
        [1, 4, 6] ,
        [1, 5, 0] ,
        [1, 6, 0] ,
        [1, 7, 0] ,
        [1, 8, 0] ,
        [1, 9, 0] ,
        [1, 10, 0] ,
        [1, 11, 0] ,
        [2, 0, 0] ,
        [2, 1, 0] ,
        [2, 3, 8] ,
        [2, 4, 0] ,
        [2, 5, 0] ,
        [2, 6, 9] ,
        [2, 7, 0] ,
        [2, 8, 0] ,
        [2, 9, 0] ,
        [2, 10, 0] ,
        [2, 11, 0] ,
        [3, 0, 5] ,
        [3, 1, 0] ,
        [3, 2, 8] ,
        [3, 4, 7] ,
        [3, 5, 10] ,
        [3, 6, 0] ,
        [3, 7, 0] ,
        [3, 8, 0] ,
        [3, 9, 0] ,
        [3, 10, 0] ,
        [3, 11, 0] ,
        [4, 0, 0] ,
        [4, 1, 6] ,
        [4, 2, 0] ,
        [4, 3, 7] ,
        [4, 5, 0] ,
        [4, 6, 0] ,
        [4, 7, 0] ,
        [4, 8, 0] ,
        [4, 9, 11] ,
        [4, 10, 0] ,
        [4, 11, 0] ,
        [5, 0, 0] ,
        [5, 1, 0] ,
        [5, 2, 0] ,
        [5, 3, 10] ,
        [5, 4, 0] ,
        [5, 6, 0] ,
        [5, 7, 13] ,
        [5, 8, 12] ,
        [5, 9, 0] ,
        [5, 10, 0] ,
        [5, 11, 0] ,
        [6, 0, 0] ,
        [6, 1, 0] ,
        [6, 2, 9] ,
        [6, 3, 0] ,
        [6, 4, 0] ,
        [6, 5, 0] ,
        [6, 7, 0] ,
        [6, 8, 0] ,
        [6, 9, 0] ,
        [6, 10, 14] ,
        [6, 11, 0] ,
        [7, 0, 0] ,
        [7, 1, 0] ,
        [7, 2, 0] ,
        [7, 3, 0] ,
        [7, 4, 0] ,
        [7, 5, 13] ,
        [7, 6, 0] ,
        [7, 8, 0] ,
        [7, 9, 0] ,
        [7, 10, 15] ,
        [7, 11, 0] ,
        [8, 0, 0] ,
        [8, 1, 0] ,
        [8, 2, 0] ,
        [8, 3, 0] ,
        [8, 4, 0] ,
        [8, 5, 12] ,
        [8, 6, 0] ,
        [8, 7, 0] ,
        [8, 9, 0] ,
        [8, 10, 16] ,
        [8, 11, 0] ,
        [9, 0, 0] ,
        [9, 1, 0] ,
        [9, 2, 0] ,
        [9, 3, 0] ,
        [9, 4, 11] ,
        [9, 5, 0] ,
        [9, 6, 0] ,
        [9, 7, 0] ,
        [9, 8, 0] ,
        [9, 10, 0] ,
        [9, 11, 0] ,
        [10, 0, 0] ,
        [10, 1, 0] ,
        [10, 2, 0] ,
        [10, 3, 0] ,
        [10, 4, 0] ,
        [10, 5, 0] ,
        [10, 6, 14] ,
        [10, 7, 15] ,
        [10, 8, 16] ,
        [10, 9, 0] ,
        [10, 11, 0] ,
        [11, 0, 0] ,
        [11, 1, 0] ,
        [11, 2, 0] ,
        [11, 3, 0] ,
        [11, 4, 0] ,
        [11, 5, 0] ,
        [11, 6, 0] ,
        [11, 7, 0] ,
        [11, 8, 0] ,
        [11, 9, 0] ,
        [11, 10, 0] ,
    ]
    # create graph
    graph = Graph(amount_vertices=12, starting_vertex=0)
    graph.generate_random_complete_graph()
    # graph.generate_random_complete_graph_custom(initial_path)

    # create a PSO instance
    iterations = 100
    pso = PSO(graph, iterations=iterations, size_population=30, beta=1, alpha=0.9)
    pso.run()  # runs the PSO algorithm

    # plot the outcome of running pso over the graph and save to fig
    plt.plot(range(len(pso.annotatedEvolutions)),
             pso.annotatedEvolutions, color='y')
    plt.savefig("fig.png")

	# show the GUI
    gui = GUI_G(ncount=graph.amount_vertices, edges=graph.edges,
                particles=pso.particles, gbest_evolutions=pso.evolutions,
                gbest_evolutions_annotations=pso.annotatedEvolutions)
    gui.run_path() # uncomment this line to show evolution of partticle paths, comment below
    # gui.run()

	# print the personal best of all particles
    print("After " + str(iterations) + " iterations :")
    print("---------------------------------------------------------------")
    pso.show_particles()  # shows the particles

	# print the global best parameters after completion of iterations
    print('gbest: %s | cost: %d\n' % (pso.get_gbest().get_pbest(),
          pso.get_gbest().get_cost_pbest()))  # shows the global best particle
