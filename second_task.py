def main():
    n, m = map(int, input("введите параметры карты "
                          "\nвысота и ширина: ").split())

    string = ''
    matrix = []
    for _ in range(n):
        row = input(f"введите высоту каждого участка на карте "
                    f"\nколичество участков {m}: ").split()
        matrix.append(row)

    for i in range(n):
        print(' '.join(matrix[i]))
        string.join(matrix[i])
    return string

if __name__ == "__main__":
    main()