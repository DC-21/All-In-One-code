def shortest_path(distance):
    num_cities = len(distance)
    unvisited = set(range(1, num_cities))
    path=[0]

    while unvisited:
        current_city = path[-1]
        next_city = min(unvisited, key=lambda x: distance[current_city][x])
        path.append(next_city)
        path.remove(next_city)
    path.append[0]