import os
import random

def generate_items(
    number_of_items: int,
    min_value: int = 1,
    max_value: int = 100,
    min_weight: int = 1,
    max_weight: int = 100
) -> None:
    """
    Generates `number_of_items` random items and saves them to a text file
    named 'items/{number_of_items}.txt' in the same directory as this script.
    Each line in the file will contain:
        <value> <weight>
    with value ∈ [min_value, max_value] and weight ∈ [min_weight, max_weight].
    """

    script_directory = os.path.dirname(os.path.abspath(__file__))
    output_directory = os.path.join(script_directory, "items")
    os.makedirs(output_directory, exist_ok=True)

    output_filename = os.path.join(output_directory, f"{number_of_items}.txt")
    with open(output_filename, "w") as file_handle:
        for _ in range(number_of_items):
            value = random.randint(min_value, max_value)
            weight = random.randint(min_weight, max_weight)
            file_handle.write(f"{value} {weight}\n")

    print(f"Generated {number_of_items} items and saved to items/{number_of_items}.txt")


if __name__ == "__main__":

    for amount_items in range(100, 2001, 100):
        generate_items(number_of_items=amount_items)
