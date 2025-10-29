def main():
    n = int(input("введите количество платформ: "))
    h = list(map(int, input(f"введите высоту платформ ({n} штук) ").split()))

    result = [-1] * n

    # Обрабатываем чётные и нечётные индексы отдельно
    for parity in (0, 1):
        stack = []
        # Идём справа налево по индексам данной чётности
        for idx in range(n - 1, -1, -1):
            if idx % 2 != parity:
                continue
            # Удаляем из стека индексы, у которых высота <= текущей
            while stack and h[stack[-1]] <= h[idx]:
                stack.pop()
            if stack:
                result[idx] = stack[-1] - idx
            stack.append(idx)

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()