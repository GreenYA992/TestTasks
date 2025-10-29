def main():
    n, m = map(int, input("Введите количество островов и через пробел количество туннелей: ").split())
    treasures = list(map(int, input("введите стоимость сокровищ на каждом острове: ").split()))

    """
    # input.txt вместо консоли
    with open('input.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        treasures = list(map(int, f.readline().split()))
    """

    # Создаем список смежности
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input("введите туннели между островами: ").split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    max_value = 0
    stack = []

    # Начинаем с острова 1 (индекс 0)
    start = 1 << 0
    stack.append((start, 0, treasures[0]))

    while stack:
        mask, current, value = stack.pop()
        max_value = max(max_value, value)

        # Пытаемся пойти в соседние острова
        for neighbor in graph[current]:
            if not (mask & (1 << neighbor)):
                new_mask = mask | (1 << neighbor)
                stack.append((new_mask, neighbor, value + treasures[neighbor]))

    print(max_value)
    return max_value


#if __name__ == "__main__":
    #main()