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
    return path
distance = [[1,2,3,4],
[0,1,2,3],
[1,0,2,1],
[0,0,1,2]]

path = shortest_path(distance)
print(path)