def greedy(capacity: int, containers: list[dict]) -> tuple[int, list[dict]]:

    containers.sort(key=lambda c: c['value']/c['weight'], reverse=True)

    i = 0
    value = 0
    used_capacity = 0
    loaded_containers = []
    while i < len(containers) and capacity - used_capacity > 0:

        container = containers[i]
        if used_capacity + container['weight'] <= capacity:
            loaded_containers.append(container)
            used_capacity += container['weight']
            value += container['value']

        i += 1

    return value, loaded_containers


def dynamic(capacity: int, containers: list[dict]):
    """
    Rozwiązuje problem plecakowy metodą programowania dynamicznego (bottom-up).

    Zwraca:
        value (int) - maksymalna wartość ładunku,
        loaded_containers (list[dict]) - lista wybranych kontenerów.
    """
    # 1) Przygotuj tabelę dp; wiersze: 0…len(containers), kolumny: 0…capacity
    dp = [
        [0] * (capacity + 1)
        for _ in range(len(containers) + 1)
    ]

    # 2) Wypełnij tabelę
    for i in range(1, len(containers) + 1):
        container = containers[i - 1]
        weight = container['weight']
        cont_value = container['value']

        for c in range(capacity + 1):
            # opcja: nie bierzemy i-tego kontenera
            dp[i][c] = dp[i - 1][c]

            # opcja: bierzemy i-ty kontener, jeśli się mieści
            if weight <= c:
                candidate_value = dp[i - 1][c - weight] + cont_value
                if candidate_value > dp[i][c]:
                    dp[i][c] = candidate_value

    # 3) Odczytaj maksymalną wartość
    value = dp[len(containers)][capacity]

    # 4) Rekonstrukcja listy załadowanych kontenerów
    loaded_containers: list[dict] = []
    remaining_capacity = capacity

    for i in range(len(containers), 0, -1):
        if dp[i][remaining_capacity] != dp[i - 1][remaining_capacity]:
            container = containers[i - 1]
            loaded_containers.append(container)
            remaining_capacity -= container['weight']

    loaded_containers.reverse()
    return value, loaded_containers, dp


if __name__ == '__main__':

    num_elements = int(input('Ile elementów? '))
    sizes = list(map(int, input('Rozmiary ').split()))
    values = list(map(int, input('Wartości ').split()))
    backpack_size = int(input('Rozmiar plecaka: '))

    items = []
    for i in range(num_elements):
        items.append({'id': i, 'weight': sizes[i], 'value': values[i]})

    max_value, loaded_containers, dp = dynamic(backpack_size, items)
    
    print(f'Max wartość: {max_value}\n\nTablica wartośći pośrednich:')
    for line in dp:
        print(line)
        