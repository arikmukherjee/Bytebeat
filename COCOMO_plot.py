import os
import matplotlib.pyplot as plt
import numpy as np

def count_lines_of_code(directory):
    """Count the total lines of code (KLOC) in the project directory."""
    total_lines = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                filepath = os.path.join(dirpath, filename)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                    lines = file.readlines()
                    total_lines += len(lines)
    return total_lines / 1000  # Convert to KLOC

def calculate_cocomo_basic(size):
    """Calculate COCOMO metrics based on KLOC size."""
    if 2 <= size <= 50:
        model_index = 0  # Organic
        mode = "Organic"
    elif 50 < size <= 300:
        model_index = 1  # Semi-Detached
        mode = "Semi-Detached"
    elif size > 300:
        model_index = 2  # Embedded
        mode = "Embedded"
    else:
        print("Size must be greater than or equal to 2 KLOC.")
        return None

    table = [
        [2.4, 1.05, 2.5, 0.38],  # Organic
        [3.0, 1.12, 2.5, 0.35],  # Semi-Detached
        [3.6, 1.20, 2.5, 0.32]   # Embedded
    ]
    
    print(f"The mode is: {mode}")

    # Calculate Effort
    effort = table[model_index][0] * (size ** table[model_index][1])

    # Calculate Development Time
    time = table[model_index][2] * (effort ** table[model_index][3])

    # Calculate Average Staff Required
    staff = effort / time

    return effort, time, staff

def plot_kloc_vs_metrics(kloc_values, efforts, times, staffs):
    """Plot KLOC and its associated metrics using matplotlib."""
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
    axes = axes.flatten()

    metrics = ['Effort', 'Duration', 'People']
    titles = ['Effort vs. KLOC', 'Duration vs. KLOC', 'People vs. KLOC']
    units = ['Effort (Person-Months)', 'Duration (Months)', 'People (Persons)']

    for i, metric in enumerate([efforts, times, staffs]):
        axes[i].plot(kloc_values, metric)
        axes[i].set_title(titles[i])
        axes[i].set_xlabel('KLOC')
        axes[i].set_ylabel(units[i])
        axes[i].grid(True)

    plt.tight_layout()
    plt.show()

def main():
    directory = input("Enter the path to the Python project directory: ")

    if not os.path.isdir(directory):
        print("Invalid directory. Please enter a valid path.")
        return

    # Count lines of code in the project
    loc = count_lines_of_code(directory)
    print(f"Total lines of code (KLOC): {round(loc, 2)} KLOC")

    # Calculate COCOMO metrics for the given KLOC
    result = calculate_cocomo_basic(loc)
    
    if result:
        effort, time, staff = result

        print(f"Effort = {round(effort)} Person-Months")
        print(f"Development Time = {round(time)} Months")
        print(f"Average Staff Required = {round(staff)} Persons")

        # Plot the results for a range of KLOC
        kloc_values = np.linspace(2, 500, 100)  # Range of KLOC from 2 to 500
        efforts = []
        times = []
        staffs = []

        for kloc in kloc_values:
            effort, time, staff = calculate_cocomo_basic(kloc)
            efforts.append(effort)
            times.append(time)
            staffs.append(staff)

        # Plot the KLOC vs metrics
        plot_kloc_vs_metrics(kloc_values, efforts, times, staffs)

if __name__ == "__main__":
    main()
