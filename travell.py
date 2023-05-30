def shortest_path(distance):
    num_cities = len(distance)
    unvisited = set(range(1, num_cities))
    path=[0]

    while unvisited: