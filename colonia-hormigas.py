import random

class AntColony:
    def __init__(self, graph, num_ants, num_iterations, decay, alpha=1, beta=1):
        self.graph = graph
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        self.pheromone = [[1 / (len(graph) * len(graph)) for _ in range(len(graph))] for _ in range(len(graph))]

    def run(self):
        shortest_path = None
        all_time_shortest_path = ("placeholder", float('inf'))
        for i in range(self.num_iterations):
            all_paths = self.construct_all_paths()
            self.spread_pheromone(all_paths, self.decay)
            shortest_path = min(all_paths, key=lambda x: x[1])
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path
        return all_time_shortest_path

    def construct_all_paths(self):
        all_paths = []
        for _ in range(self.num_ants):
            path = self.construct_path(0)
            all_paths.append((path, self.path_length(path)))
        return all_paths

    def construct_path(self, start):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for _ in range(len(self.graph) - 1):
            move = self.pick_move(self.pheromone[prev], self.graph[prev], visited)
            path.append((prev, move))
            prev = move
            visited.add(move)
        path.append((prev, start))  # volver a donde iniciamos
        return path

    def pick_move(self, pheromone, distances, visited):
        pheromone = [p ** self.alpha for p in pheromone]
        distances = [1 / d if d != 0 else 0 for d in distances]
        probabilities = [p * d for p, d in zip(pheromone, distances)]
        probabilities = [p if i not in visited else 0 for i, p in enumerate(probabilities)]
        total = sum(probabilities)
        probabilities = [p / total for p in probabilities]
        move = random.choices(range(len(self.graph)), probabilities)[0]
        return move

    def path_length(self, path):
        total_length = 0
        for (i, j) in path:
            total_length += self.graph[i][j]
        return total_length

    def spread_pheromone(self, all_paths, decay):
        for path, length in all_paths:
            for move in path:
                self.pheromone[move[0]][move[1]] += 1.0 / length
        for i in range(len(self.pheromone)):
            for j in range(len(self.pheromone)):
                self.pheromone[i][j] *= (1 - decay)

if __name__ == "__main__":
    graph = [
        [0, 2, 2, 5, 7],
        [2, 0, 4, 8, 2],
        [2, 4, 0, 1, 3],
        [5, 8, 1, 0, 2],
        [7, 2, 3, 2, 0]
    ]
    ant_colony = AntColony(graph, num_ants=10, num_iterations=100, decay=0.5, alpha=1, beta=2)
    shortest_path = ant_colony.run()
    print("shortest_path: {}".format(shortest_path))