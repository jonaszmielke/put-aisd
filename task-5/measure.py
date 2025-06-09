import os
import sys
import time

# allow import from parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from knapsack import greedy, dynamic
from save_results import save_results


def read_items(number_of_items: int):
    """
    Reads items from 'items/{number_of_items}.txt'.
    Each line in the file must be "<value> <weight>".
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'items', f"{number_of_items}.txt")

    containers = []
    with open(input_path, "r") as file_handle:
        for idx, line in enumerate(file_handle):
            line = line.strip()
            if not line:
                continue
            value_str, weight_str = line.split()
            containers.append({
                "id": idx + 1,
                "value": int(value_str),
                "weight": int(weight_str)
            })
    return containers

def main():
    algorithms = [
        {'name': 'greedy',  'algo': greedy},
        {'name': 'dynamic', 'algo': dynamic}
    ]

    # Ranges for testing
    item_range = range(100, 2001, 100)     # 100, 200, …, 2000
    capacity_range = range(100, 2001, 100) # 100, 200, …, 2000
    # Number of repeats to average over
    NUM_RUNS = 50

    # Calculate total number of tests for logging
    total_tests = len(algorithms) * (len(item_range) + len(capacity_range))

    # Prepare result containers
    results_a = {'greedy': {}, 'dynamic': {}}
    results_b = {'greedy': {}, 'dynamic': {}}

    test_counter = 1

    # Scenario A: constant capacity, vary number of items
    capacity_constant = 1000
    for algorithm in algorithms:
        for num_items in item_range:
            print(f"({test_counter}/{total_tests}) "
                  f"Measuring {algorithm['name']} with {num_items} items…")
            containers = read_items(num_items)

            total_time = 0.0
            value = None
            for _ in range(NUM_RUNS):
                start = time.perf_counter()
                value, _ = algorithm['algo'](capacity_constant, containers)
                total_time += time.perf_counter() - start

            avg_time = total_time / NUM_RUNS
            results_a[algorithm['name']][num_items] = {
                'value': value,
                'time': avg_time
            }
            print(f"    Done {NUM_RUNS} runs, avg time = {avg_time*1000:.2f} ms, value = {value}\n")
            test_counter += 1

    # Scenario B: constant number of items, vary capacity
    num_items_constant = 1000
    for algorithm in algorithms:
        for capacity in capacity_range:
            print(f"({test_counter}/{total_tests}) "
                  f"Measuring {algorithm['name']} with capacity={capacity}…")
            containers = read_items(num_items_constant)

            total_time = 0.0
            value = None
            for _ in range(NUM_RUNS):
                start = time.perf_counter()
                value, _ = algorithm['algo'](capacity, containers)
                total_time += time.perf_counter() - start

            avg_time = total_time / NUM_RUNS
            results_b[algorithm['name']][capacity] = {
                'value': value,
                'time': avg_time
            }
            print(f"    Done {NUM_RUNS} runs, avg time = {avg_time*1000:.2f} ms, value = {value}\n")
            test_counter += 1

    # Save and plot results
    save_results(
        results_dict=results_a,
        x_label="Number of Items",
        x_key="number_of_items",
        scenario_name="constant_capacity"
    )
    save_results(
        results_dict=results_b,
        x_label="Capacity",
        x_key="capacity",
        scenario_name="constant_item_count"
    )

if __name__ == '__main__':
    main()
