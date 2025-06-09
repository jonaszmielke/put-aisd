import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time

from knapsack import greedy, dynamic
from save_results import save_results


def read_items(number_of_items: int):
   
    input_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'items', f"{number_of_items}.txt")

    containers = []
    with open(input_filename, "r") as file_handle:
        for index, line in enumerate(file_handle):
            stripped_line = line.strip()
            if not stripped_line:
                continue
            value_str, weight_str = stripped_line.split()
            containers.append({
                "id": index + 1,
                "value": int(value_str),
                "weight": int(weight_str)
            })

    return containers


def main():

    all_time_start = time.perf_counter()
    algorithms = [{'name': 'greedy', 'algo': greedy}, {'name': 'dynamic', 'algo': dynamic}]

    # constant knapsack capacity, amount of items changes
    results_a = {
        'greedy': {},
        'dynamic': {}
    }
    # knapsack capacity changes, constant amount of items
    results_b = {
        'greedy': {},
        'dynamic': {}
    }
    i = 1

    #test a
    for algorithm in algorithms:

        capacity = 1000
        for num_containers in range(100, 2001, 100):

            print(f'({i}/{80}) Mesuring {algorithm['name']}')
            result = {}
            containers = read_items(num_containers)

            start_time = time.perf_counter()
            result['value'], chosen_containers = algorithm['algo'](capacity, containers)
            end_time = time.perf_counter()

            result['time'] = end_time - start_time
            
            results_a[algorithm['name']][num_containers] = result
            time_taken = (end_time - start_time) * 1000
            print(f'Finished. Took {time_taken:.2f} ms\n\n')
            i += 1

    #test b
    for algorithm in algorithms:

        num_containers = 1000
        for capacity in range(100, 2001, 100):
        
            print(f'({i}/{80}) Mesuring {algorithm['name']}')
            result = {}
            containers = read_items(num_containers)

            start_time = time.perf_counter()
            result['value'], chosen_containers = algorithm['algo'](capacity, containers)
            end_time = time.perf_counter()

            result['time'] = end_time - start_time
            
            results_b[algorithm['name']][capacity] = result
            time_taken = (end_time - start_time) * 1000
            print(f'Finished. Took {time_taken:.2f} ms\n\n')
            i += 1


    all_time_end = time.perf_counter()
    all_time = (all_time_end - all_time_start) * 1000
    print(f'All tests completed. \nTook {all_time:.2f} ms\n\n')


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