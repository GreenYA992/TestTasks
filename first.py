import heapq

def main():
    n, m = map(int, input().split())

    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Используем min-heap вместо очереди
    heap = []
    flood_time = [[10 ** 18] * m for _ in range(n)]

    # Изначально вода там, где высота = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                flood_time[i][j] = 0
                heapq.heappush(heap, (0, i, j))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while heap:
        time, x, y = heapq.heappop(heap)

        # Если это устаревшее значение, пропускаем
        if time != flood_time[x][y]:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                # Время затопления соседа = max(время затопления текущей клетки + 1, высота соседа)
                new_time = max(time + 1, matrix[nx][ny])

                if new_time < flood_time[nx][ny]:
                    flood_time[nx][ny] = new_time
                    heapq.heappush(heap, (new_time, nx, ny))

    # Выводим результат
    for i in range(n):
        print(' '.join(map(str, flood_time[i])))


if __name__ == "__main__":
    main()