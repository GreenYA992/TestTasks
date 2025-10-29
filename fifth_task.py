def main():
    n, k = map(int, input("количество дата-центров и количество соединений ").split())
    g = [[] for _ in range(n)]

    # Читаем рёбра
    for _ in range(k):
        a, b = map(int, input("номера соединенных дата-центров").split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    # Поиск мостов
    timer = 0
    tin = [-1] * n
    low = [-1] * n
    bridges = []

    def dfs(v, p):
        nonlocal timer
        tin[v] = timer
        low[v] = timer
        timer += 1
        for to in g[v]:
            if to == p:
                continue
            if tin[to] == -1:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.append((v, to))
            else:
                low[v] = min(low[v], tin[to])

    dfs(0, -1)

    # Находим компоненты связности после удаления мостов
    comp = [-1] * n
    comp_id = 0

    def dfs_comp(v, cid):
        stack = [v]
        comp[v] = cid
        while stack:
            u = stack.pop()
            for to in g[u]:
                if comp[to] == -1:
                    # Проверяем, не мост ли это ребро
                    is_bridge = (u, to) in bridges or (to, u) in bridges
                    if not is_bridge:
                        comp[to] = cid
                        stack.append(to)

    for i in range(n):
        if comp[i] == -1:
            dfs_comp(i, comp_id)
            comp_id += 1

    # Строим дерево компонент
    tree = [[] for _ in range(comp_id)]
    for a, b in bridges:
        tree[comp[a]].append(comp[b])
        tree[comp[b]].append(comp[a])

    # Находим листья в дереве компонент
    leaves = []
    for i in range(comp_id):
        if len(tree[i]) == 1:
            leaves.append(i)

    # Минимальное количество новых соединений
    m = (len(leaves) + 1) // 2
    print(m)

    # Соединяем листья
    for i in range(m):
        # Соединяем i-й лист с (i + m)-м листом
        # Если выходим за границы - соединяем с первым
        j = i + m
        if j >= len(leaves):
            j = 0
        print(leaves[i] + 1, leaves[j] + 1)


if __name__ == "__main__":
    main()