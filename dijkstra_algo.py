def dijkstra(mapping, dest, src):
    # Init les noeuds
    dist = {city: float(' inf ') for city in mapping}
    dist[src] = 0
    next_city = [src]
    visited_city = []

    # Tant qu'il y a des sommets
    while len(next_city) > 0:
        sorted_city = sorted(next_city, key=lambda v: dist[v])
        current_town = sorted_city[0]

        if current_town == dest:
            return dist[dest]

        for neighbour, distance in mapping[current_town].items():
            if neighbour not in visited_city:
                neighbour_dist = dist[current_town] + distance
                if neighbour_dist < dist[neighbour]:
                    dist[neighbour] = neighbour_dist
                    if neighbour not in next_city:
                        next_city.append(neighbour)
        visited_city.append(current_town)
        next_city.remove(current_town)

    return float(' inf ')
