from collections import defaultdict, deque


def main():
    n = int(input("число запросов: ").strip())

    queries = []  # список множеств слов для каждого запроса
    word_to_queries = defaultdict(list)  # слово -> список индексов запросов

    # Чтение всех запросов
    for i in range(n):
        m = int(input("число слов: ").strip())
        words = set(input("введите строку: ").strip().split())
        queries.append(words)

        # Для каждого слова запоминаем, в каких запросах оно встречается
        for word in words:
            word_to_queries[word].append(i)

    # Построим граф связей между запросами
    graph = [[] for _ in range(n)]
    for word, query_indices in word_to_queries.items():
        # Все запросы с этим словом должны быть связаны
        for i in range(len(query_indices)):
            for j in range(i + 1, len(query_indices)):
                graph[query_indices[i]].append(query_indices[j])
                graph[query_indices[j]].append(query_indices[i])

    # Найдем компоненты связности (контексты)
    visited = [False] * n
    contexts = []

    for i in range(n):
        if not visited[i]:
            # Находим все запросы в этом контексте с помощью BFS
            context_queries = []
            queue = deque([i])
            visited[i] = True

            while queue:
                current = queue.popleft()
                context_queries.append(current)

                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

            contexts.append(context_queries)

    # Для каждого контекста находим объединение всех слов
    max_context_size = 0
    for context in contexts:
        all_words = set()
        for query_idx in context:
            all_words |= queries[query_idx]  # объединяем множества слов
        max_context_size = max(max_context_size, len(all_words))

    # Выводим количество контекстов и размер самого большого
    print(len(contexts), max_context_size)
    return len(contexts), max_context_size


if __name__ == "__main__":
    main()