G = {
    "Адмиралтейская": {"Садовая": 4},
    "Садовая": {"Сенная площадь": 3, "Спасская": 3, "Адмиралтейская": 4, "Звенигородская": 5},
    "Сенная площадь": {"Садовая": 3, "Спасская": 3},
    "Спасская": {"Садовая": 3, "Сенная площадь": 3, "Достоевская": 4},
    "Звенигородская": {"Пушкинская": 3, "Садовая": 5},
    "Пушкинская": {"Звенигородская": 3, "Владимирская": 4},
    "Владимирская": {"Достоевская": 3, "Пушкинская": 4},
    "Достоевская": {"Владимирская": 3, "Спасская": 4}
}

INF = float('inf')
distances = {station: INF for station in G}
previous = {station: None for station in G}
visited = {station: False for station in G}

start_station = "Адмиралтейская"
distances[start_station] = 0

for _ in range(len(G)):
    current = min((station for station in G if not visited[station]),
                  key=lambda s : distances[s],
                  default=None)
    if current is None:
        break
    visited[current] = True

    for neighbor, weight in G[current].items():
        if not visited[neighbor]:
            new_dist = distances[current] + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current

def find_path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    return path[::-1]

end_station = "Владимирская"
path = find_path(previous, start_station, end_station)

print("Минимальные расстояния до всех станций:")
for station, distance in distances.items():
    print(f"{station}: {distance}")

print("\nКратчайший путь от", start_station, "до", end_station, ":")
print(" → ".join(path))



