import matplotlib.pyplot as plt
import numpy as np

def calculate_cocomo2(project_size, scale_factors, cost_drivers):
    # Effort calculation
    a = 2.94
    b = 0.91
    size_factor = project_size ** b

    # Calculate scale factor
    scale_factor = 1.0
    for factor in scale_factors:
        scale_factor *= factor

    effort = a * size_factor * scale_factor

    # Duration calculation
    c = 3.67
    d = 0.28
    duration = c * effort ** d

    # People calculation
    e = 1.05
    f = 0.11
    people = effort / (duration ** f) * e

    # Cost calculation
    average_salary = 8000  # Assume an average salary per person
    cost = people * average_salary

    # Adjust the cost based on cost drivers
    for driver, value in cost_drivers.items():
        cost *= value

    return {
        "Effort": effort,
        "Duration": duration,
        "People": people,
        "Cost": cost
    }

def main():
    project_size = np.linspace(1000, 100000, num=100)  #Range of project sizes
    scale_factors = [1.15, 0.95, 0.85, 0.05, 0.07]  #Scale factors (range from 0.01 to 1.00)
    cost_drivers = {
        "RELY": 1.07,  # Required software reliability
        "DATA": 0.94,  # Database size
        "CPLX": 0.80,  # Product complexity
    }

    metrics = ['Effort', 'Duration', 'People', 'Cost']
    titles = ['Effort vs. Project Size', 'Duration vs. Project Size', 'People vs. Project Size', 'Cost vs. Project Size']
    units = ['Person-Months', 'Months', 'Number of People', 'Cost (in dollars)']


    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
    axes = axes.flatten()

    for i, metric in enumerate(metrics):
        values = []
        for size in project_size:
            result = calculate_cocomo2(size, scale_factors, cost_drivers)
            values.append(result[metric])

        axes[i].plot(project_size, values)
        axes[i].set_title(titles[i])
        axes[i].set_xlabel('Project Size')
        axes[i].set_ylabel(units[i])
        axes[i].grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()