import csv
import os

def save_results(results, name_of_file):

    # Extract header keys from one of the dictionaries (assuming they all have the same keys)
    sizes = sorted(next(iter(results.values())).keys(), key=lambda x: int(x.rstrip('k')))
    header = ['Algorithm'] + sizes

    # Define the output directory (../test_results relative to the current file)
    output_dir = os.path.join(os.path.dirname(__file__), '../test_results')
    os.makedirs(output_dir, exist_ok=True)

    # Build the full path for the CSV file
    csv_path = os.path.join(output_dir, f'{name_of_file}.csv')
    
    # Write the results to the CSV file
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for algo, res in results.items():
            row = [algo] + [res[size] for size in sizes]
            writer.writerow(row)

    print(f'CSV file {name_of_file}.csv has been created')


if __name__ == '__main__':
    test_results = {
        'bubble_sort': {'1k': 0.123, '2k': 0.456, '3k': 0.789},
        'insertion_sort': {'1k': 0.234, '2k': 0.567, '3k': 0.890},
        'selection_sort': {'1k': 0.345, '2k': 0.678, '3k': 0.901}
    }

    save_results(test_results, 'test_results')
