import numpy as np

def generatesintable():
    # Set the number of entries and the range
    numentries = 1000
    xmin = 0
    x_max = 2

Calculate the step size
    step_size = (x_max - x_min) / (num_entries - 1)

Create the table with x and sin(x) values
    sin_table = []
    for i in range(num_entries):
        x = x_min + i * step_size
        sin_x = np.sin(x)
        sin_table.append((x, sin_x))

    return sin_table

def print_sin_table(sin_table):
    # Print header
    print(f"{'x':>10} {'sin(x)':>10}")
    print('-' * 22)

Print the table rows
    for x, sin_x in sin_table:
        print(f"{x:10.5f} {sin_x:10.5f}")

def main():
    sin_table = generate_sin_table()
    print_sin_table(sin_table)

if __name == "__main":
    main()
