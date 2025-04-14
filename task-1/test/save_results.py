import csv
import os

def save_results(results:dict, header:list, name_of_file:str):

    header = ['Algorithm'] + header

    # Define the output directory (../test_results relative to the current file)
    output_dir = os.path.join(os.path.dirname(__file__), '../test_results')
    os.makedirs(output_dir, exist_ok=True)

    # Build the full path for the CSV file
    csv_path = os.path.join(output_dir, f'{name_of_file}.csv')
    
    # Write the results to the CSV file
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for algorithm, result in results.items():

            row = [algorithm] + [result[amount] for amount in header[1:]]
            writer.writerow(row)

    print(f'CSV file {name_of_file}.csv has been created')




if __name__ == '__main__':
    
    test_results = {
        'bubble_sort': {'1k': 0.123, '2k': 0.456, '3k': 0.789},
        'insertion_sort': {'1k': 0.234, '2k': 0.567, '3k': 0.890},
        'selection_sort': {'1k': 0.345, '2k': 0.678, '3k': 0.901}
    }

    save_results(test_results, ['1k', '2k', '3k'],'test_results')


    test3_results = {}
    for algorithm in ['insertion_sort', 'selection_sort', 'heap_sort', 'merge_sort']:
        test3_results[algorithm] = {
            'random': 0.010,
            'ascending': 0.011,
            'descending': 0.012,
            'fixed': 0.013,
            'v-shaped': 0.014,
            'a-shaped': 0.015
        }

    save_results(test3_results, ["random", "ascending", "descending", "fixed", "v-shaped", "a-shaped"], 'test3_results')
