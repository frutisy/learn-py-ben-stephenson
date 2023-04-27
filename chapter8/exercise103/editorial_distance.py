def compute_editorial_distance(s: str, t: str) -> int:
    """Вычисляет редакционное расстояние между двумя строками."""
    if len(s) == 0:
        return len(t)

    if len(t) == 0:
        return len(s)

    cost = 0

    if s[-1] != t[-1]:
        cost = 1

    d1 = compute_editorial_distance(s[:-1], t) + 1
    d2 = compute_editorial_distance(t[:-1], s) + 1
    d3 = compute_editorial_distance(s[:-1], t[:-1]) + cost

    return min(d1, d2, d3)


def main():
    s = input("Введите первую строку: ")
    t = input("Введите вторую строку: ")

    distance = compute_editorial_distance(s, t)

    print(f"Редакционное расстояние между строками {s} и {t} равно {distance}")


if __name__ == '__main__':
    main()
