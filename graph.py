class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = {}

    def add_edge(self, to_data, time, cost):
        self.edges[to_data] = {"time": time, "cost": cost}

    def get_edges(self):
        return self.edges.keys()

    def get_weight(self, vertex_b ):
        return self.edges[vertex_b]["time"], self.edges[vertex_b]["cost"]


class Graph:
    def __init__(self, dircted = False):
        self.vertices = {} #empty Graph
        self.dircted = dircted

    def add_vertex(self, vertex):
        self.vertices[vertex.data] = vertex

    def add_edge(self, vertex_a, vertex_b, time, cost ):
        self.vertices[vertex_a.data].add_edge(vertex_b.data, time, cost)
        if not self.dircted:
            self.vertices[vertex_b.data].add_edge(vertex_a.data, time, cost)

    def get_edges(self, vertex):
        return self.vertices[vertex.data].get_edges()

    def get_weight(self, vertex_a, vertex_b):
        return self.vertices[vertex_a].get_weight(vertex_b)

    def path_exists(self, vertex_a, vertex_b):
        to_check = [vertex_a]
        checked = []

        while to_check:
            current = to_check.pop(0)
            checked.append(current)
            if current == vertex_b:
                return True
            else:
                options = self.vertices[current].get_edges()
                to_check += [vertex for vertex in options if vertex not in checked]
        return False


def get_path(flights_graph, vertex_a, vertex_b, path=[]):
    current = vertex_a
    path = path + [current]

    if current == vertex_b:
        return path
    for vertex in flights_graph.vertices[current].get_edges():
        if vertex not in path:
            new_path = get_path(flights_graph, vertex, vertex_b, path)
            if new_path:
                return new_path


cities = ['Kuwait', "Dubai", "Colombo", "Male", "Doha", "Tokyo", "Oslo"]
        #   [ 0,        1 ,        2 ,      3,      4 ,     5,      6   ]
cities = [ Vertex(city) for city in cities ]

flights_graph = Graph()

for city in cities:
     flights_graph.add_vertex(city)

flights_graph.add_edge( cities[0], cities[1], 2, 120)
flights_graph.add_edge( cities[0], cities[2], 4, 200)
flights_graph.add_edge( cities[2], cities[3], 1, 60)
flights_graph.add_edge( cities[1], cities[4], 1.5, 100)
flights_graph.add_edge( cities[4], cities[5], 11, 500)
flights_graph.add_edge( cities[1], cities[6], 6, 300)


print("--"*50 + "\n******** Wlcome to Coded Airlines ********\n       where flights are imaginary \n" + "--"*50+"\n\n")
print("Our airline has multiple flights. \n ")

for i,c in enumerate(flights_graph.vertices.keys()):
    print(f"{i}. {c}")

from_c = int(input("\nPlease write down the (number) of the city you wanna travel from: "))

choice = input("\nDo you want direct flights? (1) or indirect flights? (2) ")



if choice == "1":
    print(f"\nDirect flights from {cities[from_c].data} can go to: ")

    for i,c in enumerate(flights_graph.get_edges(cities[from_c])):
        print(f"{i}. {c}")
    to_options = [city for city in flights_graph.get_edges(cities[from_c])]

    to_c = int(input("\nWhere do you wanna go? (the number) "))

    time, cost = flights_graph.get_weight(cities[from_c].data, to_options[to_c])
    print("\n"+ "--"*50)
    print(f"Trip from: {cities[from_c].data} to: {to_options[to_c]} \nTotal: {cost}$   ||   Duration: {time} hours")
    print("--"*50+"\n")

else:

    to_cities = [ city.data for city in cities if flights_graph.path_exists(cities[from_c].data, city.data) and cities[from_c].data != city.data]

    print(f"\nFrom {cities[from_c].data} you can go to: ")
    for i,c in enumerate(to_cities):
        print(f"{i}. {c}")

    to_c = int(input("\nWhere do you wanna go? (the number) "))

    path = get_path(flights_graph, cities[from_c].data, to_cities[to_c])
    total_cost = 0
    total_time =0
    for i in range(0,len(path)-1,1):
        time, cost = flights_graph.get_weight(path[i], path[i+1])
        print(f"\n\nFlight{i+1} -> From: {path[i]} To: {path[i+1]} ||  Cost: {cost}$   &  Duration: {time} hours" )
        total_cost += cost
        total_time += time

    print("\nSummary:\n" + "--"*50 + f"\nA flight From: {cities[from_c].data} To: {to_cities[to_c]} would have a total Cost: {total_cost}$   &  Duration: {total_time} hours\n" + "--"*50 )
