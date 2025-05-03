import os
import random

def parse_count(s):
    """Parse a string like '10m', '100k', or '500' into an integer count."""
    s = s.strip()
    if s[-1].lower() == 'k':
        return int(s[:-1]) * 1000
    elif s[-1].lower() == 'm':
        return int(s[:-1]) * 1000000
    else:
        return int(s)

def generate_random(n):
    """Generate a list of n random integers from 0 to 2^31 - 1."""
    max_int = 2**31 - 1
    return [random.randint(0, max_int) for _ in range(n)]

def generate_ascending(n):
    """Generate an ascending sorted list of n numbers (0 to n-1)."""
    return list(range(n))

def generate_descending(n):
    """Generate a descending sorted list of n numbers (n-1 down to 0)."""
    return list(range(n-1, -1, -1))

def generate_fixed(n, fixed_value=42):
    """Generate a list of n identical numbers (default 42)."""
    return [fixed_value] * n

def generate_v_shaped(n):
    """
    Generate a V-shaped list: values decrease until the center, then increase.
    For example, for n=7: [3, 2, 1, 0, 1, 2, 3]
    """
    mid = n // 2
    return [abs(i - mid) for i in range(n)]

def generate_a_shaped(n):
    """
    Generate an A-shaped list: values increase until the center, then decrease.
    For example, for n=7: [0, 1, 2, 3, 2, 1, 0]
    """
    mid = n // 2
    return [mid - abs(i - mid) for i in range(n)]

def write_dataset(data, dataset_type, count_str):
    """Save the data list to datasets/<dataset_type>/<count_str>.txt."""
    directory = os.path.join("datasets", dataset_type)
    os.makedirs(directory, exist_ok=True)
    filename = os.path.join(directory, f"{count_str}.txt")
    with open(filename, "w") as f:
        for num in data:
            f.write(f"{num}\n")
    print(f"Wrote dataset '{dataset_type}' with {len(data)} elements to {filename}")



def generate_datasets(selected:str, count_str:str):

    generators = {
        "random": generate_random,
        "ascending": generate_ascending,
        "descending": generate_descending,
        "fixed": generate_fixed,
        "v-shaped": generate_v_shaped,
        "a-shaped": generate_a_shaped,
    }
    
    try:
        n = parse_count(count_str)
    except ValueError:
        print("Invalid input. Please enter a number optionally ending with 'k' or 'm'.")
        return


    if selected.lower() == 'all':

        for ds_type, gen_func in generators.items():
            print(f"Generating {ds_type} dataset with {n} elements...")
            data = gen_func(n)
            write_dataset(data, ds_type, count_str)

    elif selected in generators.keys():

        print(f"Generating {selected} dataset with {n} elements...")
        data = generators[selected](n)
        write_dataset(data, selected, count_str)

    else:
        print('An incorrect option was selected')




def main():

    generators = ["random", "ascending", "descending", "fixed", "v-shaped", "a-shaped"]

    print("Select the type of dataset to generate:\nAvailable types:")
    i = 1
    for ds_type in generators:
        print(f"{i}) {ds_type}")
        i += 1
    print(f"{i}) all\n")

    selected = input('Provide a name or a number: ')
    count_str = input("Enter the number of elements (e.g. 10m, 100k, or 500): ").strip()

    if selected.isdigit():

        if selected == f'{i}':
            selected = 'all'

        elif int(selected) < i:
            print('An incorrect option was selected')
            return
        
        else:
            selected = generators[int(selected)-1]

    generate_datasets(selected, count_str)


if __name__ == "__main__":

    choice = input('Generate predefined or custom?\np for predefined, c for custom: ')
    if choice == 'p':

        #test1 i 
        #random 1-15k
        #for i in range(10,26):
        #    generate_datasets('random', f'{i}k')


        #test2
        for i in range(1,16):
            generate_datasets('random', f'{i}m')
        
        #test3
        #all 1k
        #generate_datasets('all', '1k')

        #test4
        #a-shaped 1m
        #generate_datasets('a-shaped', '1m')


    elif choice == 'c':
        main()
    