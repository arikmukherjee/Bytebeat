# **1. Cocomo Basic**

**Write a Program to Demonstrate Basic COCOMO Model.**

def calculate_cocomo_basic(table, modes, size):
    """
    Calculate the effort, development time, and average staff required
    for a software project using the Basic COCOMO model.

    Parameters:
    table (list): A 2D list containing model parameters.
    modes (list): A list of mode names.
    size (float): The size of the software in thousands of lines of code (KLOC).
    """
    # Determine the model based on the size
    if 2 <= size <= 50:
        model_index = 0  # Organic
    elif 50 < size <= 300:
        model_index = 1  # Semi-Detached
    elif size > 300:
        model_index = 2  # Embedded
    else:
        print("Size must be greater than or equal to 2 KLOC.")
        return

    print(f"The mode is: {modes[model_index]}")

    # Calculate Effort
    effort = table[model_index][0] * (size ** table[model_index][1])

    # Calculate Development Time
    time = table[model_index][2] * (effort ** table[model_index][3])

    # Calculate Average Staff Required
    staff = effort / time

    # Output the calculated values
    print(f"Effort = {round(effort)} Person-Months")
    print(f"Development Time = {round(time)} Months")
    print(f"Average Staff Required = {round(staff)} Persons")


def main():
    # COCOMO model parameters for different modes
    table = [
        [2.4, 1.05, 2.5, 0.38],  # Organic
        [3.0, 1.12, 2.5, 0.35],  # Semi-Detached
        [3.6, 1.20, 2.5, 0.32]   # Embedded
    ]
    modes = ["Organic", "Semi-Detached", "Embedded"]

    # Input: Size of the software in KLOC
    try:
        size = float(input("Enter the size of the software (in KLOC): "))
        calculate_cocomo_basic(table, modes, size)
    except ValueError:
        print("Invalid input. Please enter a numeric value for size.")

if __name__ == "__main__":
    main()






###############################################################################################################################################################
"""# **2.COCOMO Basic Plot**

**Write a Program to plot the basic COCOMO Model.**
"""

import matplotlib.pyplot as plt

e1 = []
t1 = []
e2 = []
t2 = []
e3 = []
t3 = []

def calculate(table, model ,size):

	global e1,e2,e3,t1,t2,t3

	effort = 0
	time = 0

	effort = table[model][0]*pow(size, table[model][1])
	time = table[model][2]*pow(effort, table[model][3])

	if (model == 0):
		e1.append(effort)
		t1.append(time)
	elif (model == 1):
		e2.append(effort)
		t2.append(time)
	elif (model == 2):
		e3.append(effort)
		t3.append(time)

def cocomo(kloc):
	table = [[2.4,1.05,2.5,0.38],[3.0,1.12,2.5,0.35],[3.6,1.20,2.5,0.32]]
	calculate(table, 0, kloc)
	calculate(table, 1, kloc)
	calculate(table, 2, kloc)

def main():
	global e1,e2,e3,t1,t2,t3
	kloc = []
	for i in range(1,10000):
		kloc.append(i)
		cocomo(i)


	figure, axis = plt.subplots(1, 2)

	axis[0].plot(kloc,e1, label = 'Organic')
	axis[0].plot(kloc,e2, label = 'Semi-Detached')
	axis[0].plot(kloc,e3, label = 'Embedded')
	axis[0].set_xlabel("Size (kLOC)")
	axis[0].set_ylabel("Estimated Effort")
	axis[0].set_title("Size vs Effort")


	axis[1].plot(kloc,t1, label = 'Organic')
	axis[1].plot(kloc,t2, label = 'Semi-Detached')
	axis[1].plot(kloc,t3, label = 'Embedded')
	axis[1].set_xlabel("Size (kLOC)")
	axis[1].set_ylabel("Estimated Time (Month)")
	axis[1].set_title("Size vs Time")

	axis[0].legend()
	axis[1].legend()
	plt.show()

if __name__ == '__main__':
	main()







###############################################################################################################################################################
"""# **3.Cocomo Advance**

**Write a Program to Demonstrate Advance COCOMO Model.**
"""

import os
import fnmatch
import matplotlib.pyplot as plt

def count_lines_of_code(directory):
    total_lines = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, '*.py'):
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
                total_lines += len(lines)
    return total_lines / 1000  # Convert to KLOC

def calculate_cocomo_basic(table, model_index, size):
    # Calculate Effort
    effort = table[model_index][0] * (size ** table[model_index][1])

    # Calculate Development Time
    time = table[model_index][2] * (effort ** table[model_index][3])

    # Calculate Average Staff Required
    staff = effort / time

    return effort, time, staff

def plot_cocomo(table, modes):
    sizes = range(2, 501)  # Size range from 2 KLOC to 500 KLOC
    efforts = {mode: [] for mode in modes}
    times = {mode: [] for mode in modes}
    staffs = {mode: [] for mode in modes}

    for size in sizes:
        for i, mode in enumerate(modes):
            effort, time, staff = calculate_cocomo_basic(table, i, size)
            efforts[mode].append(effort)
            times[mode].append(time)
            staffs[mode].append(staff)

    # Plot the graphs
    plt.figure(figsize=(10, 12))

    # Plot Effort
    plt.subplot(3, 1, 1)
    for i, mode in enumerate(modes):
        plt.plot(sizes, efforts[mode], label=f'{mode} Effort', color=['blue', 'green', 'red'][i])
    plt.xlabel("Size (KLOC)")
    plt.ylabel("Effort (Person-Months)")
    plt.legend()
    plt.title("Effort vs. Size")

    # Plot Development Time
    plt.subplot(3, 1, 2)
    for i, mode in enumerate(modes):
        plt.plot(sizes, times[mode], label=f'{mode} Time', color=['blue', 'green', 'red'][i])
    plt.xlabel("Size (KLOC)")
    plt.ylabel("Development Time (Months)")
    plt.legend()
    plt.title("Development Time vs. Size")

    # Plot Average Staff
    plt.subplot(3, 1, 3)
    for i, mode in enumerate(modes):
        plt.plot(sizes, staffs[mode], label=f'{mode} Staff', color=['blue', 'green', 'red'][i])
    plt.xlabel("Size (KLOC)")
    plt.ylabel("Average Staff Required (Persons)")
    plt.legend()
    plt.title("Average Staff Required vs. Size")

    plt.tight_layout()
    plt.show()

def main():
    table = [
        [2.4, 1.05, 2.5, 0.38],  # Organic
        [3.0, 1.12, 2.5, 0.35],  # Semi-Detached
        [3.6, 1.20, 2.5, 0.32]   # Embedded
    ]
    modes = ["Organic", "Semi-Detached", "Embedded"]

    directory = input("Enter the path to the Python project directory: ")

    if not os.path.isdir(directory):
        print("Invalid directory. Please enter a valid path.")
        return

    # Count lines of code in the project
    loc = count_lines_of_code(directory)
    print(f"Total lines of code (KLOC): {round(loc, 2)} KLOC")

    # Show effort estimates for all three modes at actual size
    print("\nCOCOMO Estimates at Actual Size:")
    for i, mode in enumerate(modes):
        effort, time, staff = calculate_cocomo_basic(table, i, loc)
        print(f"\n{mode} Mode:")
        print(f"  Effort: {effort:.2f} Person-Months")
        print(f"  Development Time: {time:.2f} Months")
        print(f"  Average Staff Required: {staff:.2f} Persons")

    # Plot COCOMO metrics across size range
    plot_cocomo(table, modes)

if __name__ == "__main__":
    main()








###############################################################################################################################################################
    
"""# 3.5 **cocomo_advanced_correct** """ # run this for organic input , semi-detached , embeded  3 times 


import os
import fnmatch
import matplotlib.pyplot as plt

# --- Count LOC ---
def count_lines_of_code(directory):
    total_lines = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, '*.py'):
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
                total_lines += len(lines)
    return total_lines / 1000  # Convert to KLOC

# --- COCOMO Calculation ---
def calculate_cocomo_basic(table, model_index, size):
    effort = table[model_index][0] * (size ** table[model_index][1])
    time = table[model_index][2] * (effort ** table[model_index][3])
    staff = effort / time
    return effort, time, staff

# --- Graph Plotting (Single Model, Grid Layout) ---
def plot_cocomo_single_model(table, mode_index, mode_name):
    sizes = range(2, 501)
    efforts, times, staffs = [], [], []

    for size in sizes:
        effort, time, staff = calculate_cocomo_basic(table, mode_index, size)
        efforts.append(effort)
        times.append(time)
        staffs.append(staff)

    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(f"COCOMO Model: {mode_name}", fontsize=16)

    # Effort vs Size
    axs[0, 0].plot(sizes, efforts, color='blue')
    axs[0, 0].set_title("Effort vs Size")
    axs[0, 0].set_xlabel("Size (KLOC)")
    axs[0, 0].set_ylabel("Effort (Person-Months)")
    axs[0, 0].grid(True)

    # Time vs Size
    axs[0, 1].plot(sizes, times, color='green')
    axs[0, 1].set_title("Development Time vs Size")
    axs[0, 1].set_xlabel("Size (KLOC)")
    axs[0, 1].set_ylabel("Development Time (Months)")
    axs[0, 1].grid(True)

    # Staff vs Size
    axs[1, 0].plot(sizes, staffs, color='purple')
    axs[1, 0].set_title("Average Staff vs Size")
    axs[1, 0].set_xlabel("Size (KLOC)")
    axs[1, 0].set_ylabel("Average Staff Required")
    axs[1, 0].grid(True)

    # Empty plot (for visual symmetry)
    axs[1, 1].axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# --- Main Program ---
def main():
    # [a, b, c, d] = [effort coeff, effort exp, time coeff, time exp]
    table = [
        [2.4, 1.05, 2.5, 0.38],  # Organic
        [3.0, 1.12, 2.5, 0.35],  # Semi-Detached
        [3.6, 1.20, 2.5, 0.32]   # Embedded
    ]
    modes = ["Organic", "Semi-Detached", "Embedded"]

    directory = input("Enter the path to the Python project directory: ")
    if not os.path.isdir(directory):
        print("Invalid directory. Please enter a valid path.")
        return

    loc = count_lines_of_code(directory)
    print(f"\n✅ Total Lines of Code: {loc:.2f} KLOC")

    if loc < 2:
        print("❌ KLOC too small (<2). Must be at least 2 KLOC for COCOMO.")
        return

    # --- Determine Model ---
    if 2 <= loc <= 50:
        model_index = 0
    elif 50 < loc <= 300:
        model_index = 1
    elif loc > 300:
        model_index = 2
    else:
        print("Invalid KLOC range.")
        return

    model_name = modes[model_index]
    effort, time, staff = calculate_cocomo_basic(table, model_index, loc)

    print(f"\n📊 Estimated using COCOMO - {model_name} Model:")
    print(f"🛠 Effort Required: {effort:.2f} Person-Months")
    print(f"🕒 Development Time: {time:.2f} Months")
    print(f"👥 Average Staffing: {staff:.2f} Persons")

    # Plot graphs for selected model only
    plot_cocomo_single_model(table, model_index, model_name)

# --- Run the program ---
if __name__ == "__main__":
    main()








###############################################################################################################################################################

"""# **4.COCOMO 2 Advance**

**Write a Program to Demonstrate COCOMO 2 Advance.**
"""

import math
import matplotlib.pyplot as plt
import numpy as np

# --- COCOMO II Constants (Post-Architecture Model) ---
PARAM_A = 2.94
PARAM_B = 0.91
PARAM_C = 3.67
PARAM_D = 0.28

# --- Data Definitions ---

# Scale Factors (SF) ratings and values
SCALE_FACTORS = {
    "PREC": {"desc": "Precedentedness", "ratings": {"VL": 6.20, "L": 4.96, "N": 3.72, "H": 2.48, "VH": 1.24, "EH": 0.00}},
    "FLEX": {"desc": "Development Flexibility", "ratings": {"VL": 5.07, "L": 4.05, "N": 3.04, "H": 2.03, "VH": 1.01, "EH": 0.00}},
    "RESL": {"desc": "Architecture/Risk Resolution", "ratings": {"VL": 7.07, "L": 5.65, "N": 4.24, "H": 2.83, "VH": 1.41, "EH": 0.00}},
    "TEAM": {"desc": "Team Cohesion", "ratings": {"VL": 5.48, "L": 4.38, "N": 3.29, "H": 2.19, "VH": 1.10, "EH": 0.00}},
    "PMAT": {"desc": "Process Maturity", "ratings": {"VL": 7.80, "L": 6.24, "N": 4.68, "H": 3.12, "VH": 1.56, "EH": 0.00}},
}

# Cost Drivers (CD) ratings and multipliers
# Categories: Product, Platform, Personnel, Project
COST_DRIVERS = {
    # Product Attributes
    "RELY": {"desc": "Required Software Reliability", "ratings": {"VL": 0.82, "L": 0.92, "N": 1.00, "H": 1.10, "VH": 1.26, "EH": 1.00}}, # EH N/A in COCOMO II 2000
    "DATA": {"desc": "Database Size", "ratings": {"VL": 1.00, "L": 0.90, "N": 1.00, "H": 1.14, "VH": 1.28, "EH": 1.00}}, # VL N/A, EH N/A
    "CPLX": {"desc": "Product Complexity", "ratings": {"VL": 0.73, "L": 0.87, "N": 1.00, "H": 1.17, "VH": 1.34, "EH": 1.74}},
    "RUSE": {"desc": "Required Reusability", "ratings": {"VL": 1.00, "L": 0.95, "N": 1.00, "H": 1.07, "VH": 1.15, "EH": 1.24}}, # VL N/A
    "DOCU": {"desc": "Documentation Match to Life-Cycle Needs", "ratings": {"VL": 0.81, "L": 0.91, "N": 1.00, "H": 1.11, "VH": 1.23, "EH": 1.00}}, # EH N/A

    # Platform Attributes
    "TIME": {"desc": "Execution Time Constraint", "ratings": {"VL": 1.00, "L": 1.00, "N": 1.00, "H": 1.11, "VH": 1.29, "EH": 1.63}}, # VL, L N/A
    "STOR": {"desc": "Main Storage Constraint", "ratings": {"VL": 1.00, "L": 1.00, "N": 1.00, "H": 1.05, "VH": 1.17, "EH": 1.46}}, # VL, L N/A
    "PVOL": {"desc": "Platform Volatility", "ratings": {"VL": 1.00, "L": 0.87, "N": 1.00, "H": 1.15, "VH": 1.30, "EH": 1.00}}, # VL, EH N/A

    # Personnel Attributes
    "ACAP": {"desc": "Analyst Capability", "ratings": {"VL": 1.42, "L": 1.19, "N": 1.00, "H": 0.85, "VH": 0.71, "EH": 1.00}}, # EH N/A
    "PCAP": {"desc": "Programmer Capability", "ratings": {"VL": 1.34, "L": 1.15, "N": 1.00, "H": 0.88, "VH": 0.76, "EH": 1.00}}, # EH N/A
    "PCON": {"desc": "Personnel Continuity", "ratings": {"VL": 1.29, "L": 1.12, "N": 1.00, "H": 0.90, "VH": 0.81, "EH": 1.00}}, # EH N/A
    "APEX": {"desc": "Applications Experience", "ratings": {"VL": 1.22, "L": 1.10, "N": 1.00, "H": 0.88, "VH": 0.81, "EH": 1.00}}, # EH N/A
    "PLEX": {"desc": "Platform Experience", "ratings": {"VL": 1.19, "L": 1.09, "N": 1.00, "H": 0.91, "VH": 0.85, "EH": 1.00}}, # EH N/A
    "LTEX": {"desc": "Language and Tool Experience", "ratings": {"VL": 1.20, "L": 1.09, "N": 1.00, "H": 0.91, "VH": 0.84, "EH": 1.00}}, # EH N/A

    # Project Attributes
    "TOOL": {"desc": "Use of Software Tools", "ratings": {"VL": 1.17, "L": 1.09, "N": 1.00, "H": 0.90, "VH": 0.78, "EH": 1.00}}, # EH N/A
    "SITE": {"desc": "Multi-site Development", "ratings": {"VL": 1.22, "L": 1.09, "N": 1.00, "H": 0.93, "VH": 0.86, "EH": 0.80}},
    "SCED": {"desc": "Required Development Schedule", "ratings": {"VL": 1.43, "L": 1.14, "N": 1.00, "H": 1.00, "VH": 1.00, "EH": 1.00}}, # EH N/A
}

RATING_MAP = ["VL", "L", "N", "H", "VH", "EH"]
RATING_DESC = "(VL: Very Low, L: Low, N: Nominal, H: High, VH: Very High, EH: Extra High)"

# --- Helper Functions --- (Keep functions from previous version: get_valid_input, get_rating_input)

def get_valid_input(prompt, input_type=float, validation_func=None, allowed_values=None):
    """Gets and validates user input."""
    while True:
        try:
            user_input = input(prompt).strip()
            value = input_type(user_input)
            if validation_func and not validation_func(value):
                print("Invalid input. Please try again.")
                continue
            if allowed_values and value not in allowed_values:
                print(f"Invalid choice. Please enter one of: {', '.join(allowed_values)}")
                continue
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def get_rating_input(factor_key, factor_data):
    """Gets a valid rating (VL, L, N, H, VH, EH) for a given factor."""
    prompt = f"Enter rating for '{factor_data['desc']}' {RATING_DESC}: "
    valid_ratings = list(factor_data['ratings'].keys())
    # Ensure case-insensitivity and allow lowercase input
    allowed_input = [r.upper() for r in valid_ratings] + [r.lower() for r in valid_ratings]

    while True:
        rating = input(prompt).strip().upper()
        if rating in factor_data['ratings']:
            return rating
        else:
            print(f"Invalid rating. Please choose from: {', '.join(valid_ratings)}")

# --- Core COCOMO II Calculation Functions --- (Keep functions from previous version: calculate_scale_factor_sum, calculate_exponent_e, calculate_eaf, calculate_effort, calculate_exponent_f, calculate_tdev, calculate_staffing)

def calculate_scale_factor_sum(ratings):
    """Calculates the sum of Scale Factor values based on user ratings."""
    sf_sum = 0
    print("\n--- Calculating Scale Factor Sum ---")
    for key, rating in ratings.items():
        value = SCALE_FACTORS[key]['ratings'][rating]
        print(f"  {key} ({SCALE_FACTORS[key]['desc']}) rating '{rating}': {value:.2f}")
        sf_sum += value
    print(f"Total Sum of Scale Factors (Sum SF_i): {sf_sum:.2f}")
    return sf_sum

def calculate_exponent_e(sf_sum):
    """Calculates the exponent E."""
    e = PARAM_B + 0.01 * sf_sum
    print(f"\n--- Calculating Exponent E ---")
    print(f"  E = B + 0.01 * Sum(SF_i)")
    print(f"  E = {PARAM_B} + 0.01 * {sf_sum:.2f} = {e:.4f}")
    return e

def calculate_eaf(ratings):
    """Calculates the Effort Adjustment Factor (EAF) from Cost Driver ratings."""
    eaf = 1.0
    print("\n--- Calculating Effort Adjustment Factor (EAF) ---")
    print("  EAF = Product of all Cost Driver multipliers")
    for key, rating in ratings.items():
        # Handle cases where a rating might not exist (e.g., VL/EH N/A)
        # Defaulting to Nominal (1.0) if rating isn't applicable/defined
        multiplier = COST_DRIVERS[key]['ratings'].get(rating, 1.0)
        if multiplier == 1.0 and rating != 'N':
             print(f"  {key} ({COST_DRIVERS[key]['desc']}) rating '{rating}': {multiplier:.2f} (Nominal/Default used)")
        else:
            print(f"  {key} ({COST_DRIVERS[key]['desc']}) rating '{rating}': {multiplier:.2f}")
        eaf *= multiplier
    print(f"Total EAF: {eaf:.4f}")
    return eaf

def calculate_effort(size_kloc, exponent_e, eaf):
    """Calculates the estimated effort in Person-Months (PM)."""
    effort_pm = PARAM_A * (size_kloc ** exponent_e) * eaf
    print("\n--- Calculating Effort (PM) ---")
    print(f"  Effort = A * Size^E * EAF")
    print(f"  Effort = {PARAM_A} * ({size_kloc:.2f} KSLOC)^{exponent_e:.4f} * {eaf:.4f}")
    print(f"  Estimated Effort = {effort_pm:.2f} Person-Months")
    return effort_pm

def calculate_exponent_f(exponent_e):
    """Calculates the exponent F for the TDEV calculation."""
    f = PARAM_D + 0.2 * (exponent_e - PARAM_B)
    print("\n--- Calculating Exponent F ---")
    print(f"  F = D + 0.2 * (E - B)")
    print(f"  F = {PARAM_D} + 0.2 * ({exponent_e:.4f} - {PARAM_B}) = {f:.4f}")
    return f

def calculate_tdev(effort_pm, exponent_f):
    """Calculates the estimated time to development in Months."""
    # Handle potential edge case of zero effort
    if effort_pm <= 0:
        return 0
    tdev_months = PARAM_C * (effort_pm ** exponent_f)
    print("\n--- Calculating Time to Development (TDEV) ---")
    print(f"  TDEV = C * Effort^F")
    print(f"  TDEV = {PARAM_C} * ({effort_pm:.2f} PM)^{exponent_f:.4f}")
    print(f"  Estimated TDEV = {tdev_months:.2f} Months")
    return tdev_months

def calculate_staffing(effort_pm, tdev_months):
    """Calculates the estimated average staffing level."""
    if tdev_months <= 0:
         # Avoid division by zero if TDEV is zero or negative
        staff = 0
    else:
        staff = effort_pm / tdev_months
    print("\n--- Calculating Average Staffing ---")
    print(f"  Staff = Effort / TDEV")
    print(f"  Staff = {effort_pm:.2f} PM / {tdev_months:.2f} Months")
    print(f"  Estimated Average Staff = {staff:.2f} Persons")
    return staff

# --- Plotting Function --- (MODIFIED)

def plot_results(size_kloc, sf_ratings, cd_ratings, results):
    """Creates subplots to visualize COCOMO II results, including factor breakdowns."""
    # Increased figure size and changed layout to 3x2
    fig, axes = plt.subplots(3, 2, figsize=(16, 18)) # Adjusted size for 6 plots
    fig.suptitle('COCOMO II Post-Architecture Model Results', fontsize=18, y=0.99)

    # --- Plot 1: Summary Results (Top-Left) ---
    ax = axes[0, 0]
    summary_text = (
        f"Input Size: {size_kloc:.1f} KSLOC\n\n"
        f"--- Key Calculated Values ---\n"
        f"Sum of Scale Factors: {results['sf_sum']:.2f}\n"
        f"Calculated EAF: {results['eaf']:.3f}\n"
        f"Calculated Exponent E: {results['exponent_e']:.3f}\n"
        f"Calculated Exponent F: {results['exponent_f']:.3f}\n\n"
        f"--- Final Estimates ---\n"
        f"Effort: {results['effort_pm']:.2f} PM\n"
        f"TDEV: {results['tdev_months']:.2f} Months\n"
        f"Avg. Staff: {results['staff']:.2f} Persons"
    )
    ax.text(0.5, 0.5, summary_text, ha='center', va='center', fontsize=10, wrap=True,
            bbox=dict(boxstyle='round,pad=0.5', fc='aliceblue', alpha=0.9))
    ax.set_title('Estimation Summary')
    ax.axis('off') # Hide axes for text plot

    # --- Plot 2: Effort vs. Size (Illustrative) (Top-Right) ---
    ax = axes[0, 1]
    size_range = np.linspace(max(0.1, size_kloc * 0.5), size_kloc * 1.5, 50)
    effort_range = PARAM_A * (size_range ** results['exponent_e']) * results['eaf']
    ax.plot(size_range, effort_range, label=f'Effort Curve (E={results["exponent_e"]:.2f}, EAF={results["eaf"]:.2f})', color='royalblue')
    ax.plot(size_kloc, results['effort_pm'], 'ro', markersize=8, label=f'Calculated: {results["effort_pm"]:.1f} PM')
    ax.set_title('Effort vs. Project Size')
    ax.set_xlabel('Size (KSLOC)')
    ax.set_ylabel('Effort (Person-Months)')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)

    # --- Plot 3: TDEV vs. Effort (Illustrative) (Middle-Left) ---
    ax = axes[1, 0]
    effort_plot_range = PARAM_A * (size_range ** results['exponent_e']) * results['eaf']
    effort_plot_range_positive = np.maximum(effort_plot_range, 1e-9) # Ensure positive for power
    tdev_range = PARAM_C * (effort_plot_range_positive ** results['exponent_f'])

    ax.plot(effort_plot_range, tdev_range, label=f'TDEV Curve (F={results["exponent_f"]:.2f})', color='forestgreen')
    ax.plot(results['effort_pm'], results['tdev_months'], 'ro', markersize=8, label=f'Calculated: {results["tdev_months"]:.1f} Months')
    ax.set_title('Development Time vs. Effort')
    ax.set_xlabel('Effort (Person-Months)')
    ax.set_ylabel('TDEV (Months)')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0), useMathText=True)

    # --- Plot 4: Scale Factor Contributions (Bar Chart) (Middle-Right) ---
    ax = axes[1, 1]
    sf_names = list(sf_ratings.keys())
    sf_values = [SCALE_FACTORS[k]['ratings'][sf_ratings[k]] for k in sf_names]
    colors = plt.cm.viridis(np.linspace(0, 1, len(sf_names))) # Color map

    bars = ax.bar(sf_names, sf_values, color=colors)
    ax.set_title('Scale Factor Values (Contribution to Sum SF_i)')
    ax.set_xlabel('Scale Factor')
    ax.set_ylabel('Value (Lower values increase exponent E)')
    ax.grid(True, linestyle='--', alpha=0.6, axis='y')
    # Add value labels on top of bars
    ax.bar_label(bars, fmt='%.2f', padding=3)
    ax.set_ylim(bottom=0) # Ensure y-axis starts at 0

    # --- Plot 5: Cost Driver Multipliers (Bar Chart) (Bottom-Left) ---
    ax = axes[2, 0]
    cd_names = list(cd_ratings.keys())
    cd_multipliers = [COST_DRIVERS[k]['ratings'].get(cd_ratings[k], 1.0) for k in cd_names]
    colors = ['tomato' if m > 1.0 else 'mediumseagreen' if m < 1.0 else 'grey' for m in cd_multipliers]

    bars = ax.bar(cd_names, cd_multipliers, color=colors)
    ax.axhline(1.0, color='black', linestyle='--', linewidth=1, label='Nominal (1.0)')
    ax.set_title('Cost Driver Multipliers (Contribution to EAF)')
    ax.set_xlabel('Cost Driver')
    ax.set_ylabel('Multiplier ( >1 Increases Effort, <1 Decreases Effort)')
    ax.tick_params(axis='x', rotation=90) # Rotate labels for readability
    ax.grid(True, linestyle='--', alpha=0.6, axis='y')
    ax.legend()
    # Add value labels on top of bars
    ax.bar_label(bars, fmt='%.2f', padding=3, rotation=90, fontsize=8)
    # Adjust y-limits to better show deviations, ensuring 1.0 is visible
    min_y = min(cd_multipliers) * 0.95 if min(cd_multipliers) < 1 else 0.9
    max_y = max(cd_multipliers) * 1.05 if max(cd_multipliers) > 1 else 1.1
    ax.set_ylim(min_y, max_y)

    # --- Plot 6: Placeholder or Additional Info (Bottom-Right) ---
    # You could add more text, another plot, or leave it blank
    ax = axes[2, 1]
    influence_text = (
        f"--- Factor Influence ---\n\n"
        f"Scale Factors (Plot 4):\n"
        f"- Sum determines exponent E ({results['exponent_e']:.3f}).\n"
        f"- Lower SF values -> Higher E -> More non-linear effort increase with size.\n\n"
        f"Cost Drivers (Plot 5):\n"
        f"- Multipliers combine into EAF ({results['eaf']:.3f}).\n"
        f"- EAF directly scales the calculated effort.\n"
        f"- Red bars (>1.0) increase effort.\n"
        f"- Green bars (<1.0) decrease effort."
    )
    ax.text(0.5, 0.5, influence_text, ha='center', va='center', fontsize=10, wrap=True,
            bbox=dict(boxstyle='round,pad=0.5', fc='lightyellow', alpha=0.9))
    ax.set_title('Factor Influence Summary')
    ax.axis('off')


    plt.tight_layout(rect=[0, 0.03, 1, 0.97]) # Adjust layout further
    plt.show()


# --- Main Execution --- (Identical to previous version)

def run_cocomo_estimation():
    """Guides the user through the COCOMO II estimation process."""
    print("================================================")
    print(" COCOMO II Post-Architecture Cost Estimation Tool")
    print("================================================")

    # 1. Get Project Size
    size_kloc = get_valid_input(
        "Enter project size in KSLOC (e.g., 50.5): ",
        input_type=float,
        validation_func=lambda x: x > 0
    )

    # 2. Get Scale Factor Ratings
    print("\n--- Enter Scale Factor Ratings ---")
    sf_ratings = {}
    for key, data in SCALE_FACTORS.items():
        sf_ratings[key] = get_rating_input(key, data)

    # 3. Get Cost Driver Ratings
    print("\n--- Enter Cost Driver Ratings ---")
    print("Note: For factors where a rating is Not Applicable (N/A),")
    print("      choose the closest valid rating or Nominal (N).")
    print("      The model uses predefined multipliers for each rating.")

    cd_ratings = {}
    for key, data in COST_DRIVERS.items():
        cd_ratings[key] = get_rating_input(key, data)

    # 4. Perform Calculations
    print("\n================================================")
    print("             Starting Calculations")
    print("================================================")
    sf_sum = calculate_scale_factor_sum(sf_ratings)
    exponent_e = calculate_exponent_e(sf_sum)
    eaf = calculate_eaf(cd_ratings)
    effort_pm = calculate_effort(size_kloc, exponent_e, eaf)
    exponent_f = calculate_exponent_f(exponent_e)
    tdev_months = calculate_tdev(effort_pm, exponent_f)
    staff = calculate_staffing(effort_pm, tdev_months)

    # Store results
    results = {
        "effort_pm": effort_pm,
        "tdev_months": tdev_months,
        "staff": staff,
        "eaf": eaf,
        "exponent_e": exponent_e,
        "exponent_f": exponent_f,
        "sf_sum": sf_sum # Store sf_sum for plotting
    }

    print("\n================================================")
    print("             Final Estimation Results")
    print("================================================")
    print(f"Project Size:         {size_kloc:.2f} KSLOC")
    # print(f"Scale Factor Sum:     {sf_sum:.3f}") # Included in summary plot
    # print(f"Effort Adj. Factor:   {eaf:.3f}") # Included in summary plot
    # print(f"Exponent E:           {exponent_e:.4f}") # Included in summary plot
    # print(f"Exponent F:           {exponent_f:.4f}") # Included in summary plot
    print("------------------------------------------------")
    print(f"Estimated Effort:     {effort_pm:.2f} Person-Months")
    print(f"Estimated TDEV:       {tdev_months:.2f} Months")
    print(f"Estimated Avg Staff:  {staff:.2f} Persons")
    print("================================================")


    # 5. Plot Results
    print("\nGenerating visualization...")
    try:
        plot_results(size_kloc, sf_ratings, cd_ratings, results)
    except ImportError:
        print("\nWarning: Matplotlib not found. Skipping plot generation.")
        print("Install it using: pip install matplotlib numpy") # Added numpy dependency
    except Exception as e:
        print(f"\nAn error occurred during plotting: {e}")
        print("Skipping plot generation.")

# Execute the main function
if __name__ == "__main__":
    # Add numpy check here if desired, although ImportError handles it
    try:
        import numpy
    except ImportError:
        print("Error: NumPy library is required for plotting.")
        print("Please install it using: pip install numpy")
        exit() # Exit if numpy isn't installed, as it's needed for plotting now

    run_cocomo_estimation()










###############################################################################################################################################################

"""# **5.HALSTED**

**Write a Program to Demonstrate Halstead’s software science (effort-time and length estimation) with diagram**
"""

import math
import matplotlib.pyplot as plt

def halstead_metrics(n1, n2, N1, N2):
    n = n1 + n2
    N = N1 + N2

    if n == 0 or n2 == 0:
        raise ValueError("Vocabulary and distinct operands must be greater than 0")

    V = N * math.log2(n)
    D = (n1 / 2) * (N2 / n2)
    E = D * V
    T = E / 18
    B = V / 3000

    return {
        "Vocabulary (n)": n,
        "Program Length (N)": N,
        "Volume (V)": V,
        "Difficulty (D)": D,
        "Effort (E)": E,
        "Time to program (T seconds)": T,
        "Estimated Bugs (B)": B
    }

# Example usage
metrics = halstead_metrics(n1=82, n2=10, N1=30, N2=10)

# Print metrics
for key, value in metrics.items():
    print(f"{key}: {value:.2f}")

def plot_halstead_metrics(metrics):
    labels = list(metrics.keys())
    values = list(metrics.values())

    plt.figure(figsize=(10, 6))
    plt.plot(labels, values, marker='o', linestyle='-', color='darkgreen')
    plt.title('Halstead Metrics (Line Graph)')
    plt.xlabel('Metrics')
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Annotate values
    for i, v in enumerate(values):
        plt.text(i, v + max(values)*0.02, f"{v:.2f}", ha='center', fontsize=9)

    plt.tight_layout()
    plt.show()

# Call the plot function
plot_halstead_metrics(metrics)








###############################################################################################################################################################
"""# **6.Jensen**

**Write A Program to Demonstrate Jensen Model with diagram.**
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Core Jensen Effort Calculation ---

def calculate_jensen_effort(size_kloc, time_months, difficulty_d):
    """Effort = D * Size^3 / Time^4"""
    time_months = np.asarray(time_months)
    effort = np.full_like(time_months, float('inf'), dtype=float)
    mask = time_months > 1e-6
    effort[mask] = difficulty_d * (size_kloc ** 3) / (time_months[mask] ** 4)
    return effort if effort.size > 1 else effort.item()

# --- Plotting ---

def plot_jensen_model(nominal_size, nominal_d):
    d_variants = {"Low D (x0.7)": nominal_d * 0.7, "Nominal D": nominal_d, "High D (x1.3)": nominal_d * 1.3}
    size_variants = {"Small Size (x0.7)": nominal_size * 0.7, "Nominal Size": nominal_size, "Large Size (x1.3)": nominal_size * 1.3}
    time_range = np.linspace(3, max(24, nominal_size / 2), 100)

    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    fig.suptitle(f'Jensen Model: Effort-Time Trade-off\nNominal Size = {nominal_size:.1f} KSLOC, Nominal Difficulty = {nominal_d:.4f}', fontsize=14)

    # --- Difficulty Sensitivity Plot ---
    ax1 = axes[0]
    ax1.set_title(f'Sensitivity to Difficulty (D) at Size = {nominal_size:.1f} KSLOC')
    for label, d_val in d_variants.items():
        ax1.plot(time_range, calculate_jensen_effort(nominal_size, time_range, d_val), label=f'{label} (D={d_val:.4f})', linewidth=2)
    ax1.set(xlabel='Development Time (Months)', ylabel='Effort (Person-Months)')
    ax1.legend(); ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.set_ylim(0, calculate_jensen_effort(nominal_size, 3, d_variants["High D (x1.3)"]) * 1.1)
    ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)

    # --- Size Sensitivity Plot ---
    ax2 = axes[1]
    ax2.set_title(f'Sensitivity to Size (S) at Difficulty D = {nominal_d:.4f}')
    for label, s_val in size_variants.items():
        ax2.plot(time_range, calculate_jensen_effort(s_val, time_range, nominal_d), label=f'{label} (S={s_val:.1f} KSLOC)', linewidth=2)
    ax2.set(xlabel='Development Time (Months)', ylabel='Effort (Person-Months)')
    ax2.legend(); ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.set_ylim(0, calculate_jensen_effort(size_variants["Large Size (x1.3)"], 3, nominal_d) * 1.1)
    ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.93])
    plt.show()

# --- User Input Helper ---

def get_positive_float_input(prompt):
    while True:
        try:
            val = float(input(prompt).strip())
            if val > 0: return val
            print("Input must be positive.")
        except ValueError:
            print("Invalid number. Try again.")

# --- Main Execution ---

if __name__ == "__main__":
    print("="*40)
    print(" Jensen Software Estimation Model ")
    print(" Formula: Effort = D * Size^3 / Time^4   ")
    print("="*40)

    size = get_positive_float_input("Enter Nominal Project Size (S) in KSLOC (e.g., 100): ")
    print("\nEnter Nominal Difficulty (D) (Typical range: 0.005 to 0.1+):")
    difficulty = get_positive_float_input("Enter Nominal Difficulty (D) value (e.g., 0.03): ")

    print("\nGenerating Effort-Time trade-off plots...")
    try:
        plot_jensen_model(size, difficulty)
    except ImportError as e:
        print(f"\nMissing library: {e.name}. Install with: pip install numpy matplotlib")
    except Exception as e:
        print(f"\nAn error occurred during plotting: {e}")









###############################################################################################################################################################

"""# **7.Norden**

**Write a Program to Demonstrate Norden Model with diagram.**
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Norden Core Functions ---

def rayleigh_staffing(t, K, td):
    if td <= 1e-6:
        return np.zeros_like(t)
    exp_part = np.exp(-t**2 / (2 * td**2))
    return np.maximum((K / td**2) * t * exp_part, 0)

def rayleigh_cumulative_effort(t, K, td):
    if td <= 1e-6:
        return np.where(t > 0, K, 0)
    return np.maximum(K * (1 - np.exp(-t**2 / (2 * td**2))), 0)

# --- Plotting ---

def plot_norden_model(K, td):
    td_variants = {"Shorter td (x0.8)": td * 0.8, "Nominal td": td, "Longer td (x1.2)": td * 1.2}
    time_range = np.linspace(0, td * 2.5, 200)

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle(f'Norden Model (K={K} PM, td={td} Mo)', fontsize=15)

    # Plot 1: Nominal Staffing Curve
    ax = axes[0]
    staffing = rayleigh_staffing(time_range, K, td)
    ax.plot(time_range, staffing, color='darkred', label='Nominal Staffing')
    ax.axvline(td, linestyle='--', color='gray', label='Peak Time td')
    ax.set(title='Nominal Staffing', xlabel='Time (Months)', ylabel='Staffing Level')
    ax.legend(); ax.grid(True); ax.set_ylim(bottom=0)

    # Plot 2: Staffing Sensitivity to td
    ax = axes[1]
    for label, td_val in td_variants.items():
        ax.plot(time_range, rayleigh_staffing(time_range, K, td_val), label=label)
    ax.set(title='Staffing Sensitivity to td', xlabel='Time (Months)', ylabel='Staffing Level')
    ax.legend(); ax.grid(True); ax.set_ylim(bottom=0)

    # Plot 3: Cumulative Effort Sensitivity to td
    ax = axes[2]
    for label, td_val in td_variants.items():
        ax.plot(time_range, rayleigh_cumulative_effort(time_range, K, td_val), label=label)
    ax.set(title='Cumulative Effort Sensitivity to td', xlabel='Time (Months)', ylabel='Cumulative Effort')
    ax.axhline(K, linestyle=':', color='gray', label='Total Effort K')
    ax.legend(); ax.grid(True); ax.set_ylim(bottom=0)

    plt.tight_layout(rect=[0, 0.05, 1, 0.93])
    plt.show()

# --- Input Utility ---

def get_positive_float_input(prompt):
    while True:
        try:
            val = float(input(prompt).strip())
            if val > 0: return val
            print("Value must be positive.")
        except ValueError:
            print("Invalid number. Try again.")

# --- Main Execution ---

if __name__ == "__main__":
    print("=== Norden Model: Simplified Visualization ===")
    K = get_positive_float_input("Enter Total Effort (K) in Person-Months (e.g., 500): ")
    td = get_positive_float_input("Enter Time to Peak Staffing (td) in Months (e.g., 12): ")
    plot_norden_model(K, td)








###############################################################################################################################################################
"""# **8.Putnam**

**Write a Program to Demonstrate Putnam Model with diagram.**
"""

import numpy as np
import matplotlib.pyplot as plt

# Mapping of keyword difficulty levels to numeric D values
DIFFICULTY_MAP = {
    "VH": 0.1, "H": 0.07, "N": 0.05, "L": 0.03, "VL": 0.01
}

def get_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt).strip())
            if val > 0: return val
        except:
            pass
        print("Invalid input. Enter a positive number.")

def get_difficulty_input(prompt):
    while True:
        val = input(prompt).strip().upper()
        if val in DIFFICULTY_MAP:
            return DIFFICULTY_MAP[val]
        try:
            num = float(val)
            if num > 0: return num
        except:
            pass
        print("Invalid. Enter a numeric value or VH, H, N, L, VL.")

def putnam_effort(size_kloc, td, d):
    td = np.asarray(td)
    effort = np.full_like(td, float('inf'), dtype=float)
    mask = td > 1e-6
    effort[mask] = d * (size_kloc ** 3) / (td[mask] ** 4)
    return effort if effort.size > 1 else effort.item()

def estimate_lifecycle_effort(E, f=0.4):
    return E / f if f > 0 else 0

def rayleigh_staffing(t, K, td):
    t = np.asarray(t)
    td2 = td ** 2
    exp_term = np.exp(-t**2 / (2 * td2))
    staff = (K / td2) * t * exp_term
    return np.maximum(staff, 0)

def plot_putnam_basic(S, D, f):
    td_range = np.linspace(4, 36, 100)
    effort_curve = putnam_effort(S, td_range, D)

    # --- Plot 1: Effort vs Development Time ---
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(td_range, effort_curve, color='orange', label='Effort-Time Curve')
    plt.title("Effort vs Dev Time")
    plt.xlabel("Development Time (months)")
    plt.ylabel("Effort (PM)")
    plt.grid(True)
    plt.legend()

    # --- Plot 2: Staffing Profile for Nominal Schedule ---
    td_nom = td_range[40]  # pick a reasonable point (e.g., ~18 months)
    E_nom = putnam_effort(S, td_nom, D)
    K_nom = estimate_lifecycle_effort(E_nom, f)
    t_range = np.linspace(0, td_nom * 2.5, 200)
    staff_curve = rayleigh_staffing(t_range, K_nom, td_nom)

    plt.subplot(1, 2, 2)
    plt.plot(t_range, staff_curve, color='teal', label=f'Staffing (td={td_nom:.1f})')
    plt.title("Staffing Curve")
    plt.xlabel("Time (months)")
    plt.ylabel("Staffing Level")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.suptitle("Simplified Putnam Model", fontsize=14, y=1.05)
    plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    print("=== Simplified Putnam Model ===")
    S = get_positive_float("Enter Size (KSLOC): ")
    D = get_difficulty_input("Enter Difficulty (e.g., VH, H, N, or a number): ")
    f = get_positive_float("Enter Dev Effort Fraction (e.g., 0.4): ")

    plot_putnam_basic(S, D, f)






"""# ---*******************************************************************************************************************************************
********************************************************************************************************************************************** """







###############################################################################################################################################################
# Integration Testing


users_db = [
    {"id": 1, "name": "oggy"},
    {"id": 2, "name": "bob"},
    {"id": 3, "name": "jack"}
]


def fetch_user_data(user_id):
    for user in users_db:
        if user["id"] == user_id:
            return user
    return None

# Process the user's data (convert name to uppercase)
def process_user_data(user):
    if user:
        user["name"] = user["name"].upper()
        return user
    return None

# Integration test (all functions together)
def test_integration():
    # Step 1: Fetch data
    user = fetch_user_data(2)

    # Step 2: Process data
    processed_user = process_user_data(user)

    # Step 3: Check the result
    if processed_user:
        print(f"Processed User: {processed_user}")
        assert processed_user["name"] == "BOB"
    else:
        print("User not found.")

# Run the integration test
if __name__ == "__main__":
    test_integration()








###############################################################################################################################################################

"""# Black Box Testing"""

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance


def test_bank_account():
    print(" Starting Black-Box Testing...\n")

    acc = BankAccount(100)
    print(f" Initial Balance: ₹{acc.get_balance():.2f}\n")

    def run_test(test_no, action_text, action_func, expected_result, reason):
        actual_result = action_func
        expected_status = "SUCCEED" if expected_result else "FAIL"
        actual_status = "SUCCEEDED" if actual_result else "FAILED"
        test_pass = actual_result == expected_result
        color = "✅" if test_pass else "❌"

        print(f"🔹 Test {test_no} - Attempt: {action_text}")
        print(f"    Expected Outcome : Transaction should {expected_status} ({reason})")
        print(f"    Actual Outcome   : Transaction {actual_status}")
        print(f"    Test Result      : {color} {'PASS' if test_pass else 'FAIL'} (Correct behavior)\n")

    # Define test cases
    run_test(1, "Deposit ₹50.00", acc.deposit(50), True, "valid deposit")
    run_test(2, "Deposit ₹-10.00", acc.deposit(-10), False, "invalid deposit amount")
    run_test(3, "Withdraw ₹70.00", acc.withdraw(70), True, "valid withdrawal")
    run_test(4, "Withdraw ₹200.00", acc.withdraw(200), False, "exceeds current balance")
    run_test(5, "Withdraw ₹-20.00", acc.withdraw(-20), False, "invalid withdrawal amount")

    print("✅ All black-box test cases completed.")

if __name__ == "__main__":
    test_bank_account()








###############################################################################################################################################################
"""# McCabe Cyclomatic Complexity"""

import ast

# --- Cyclomatic Complexity Counter using AST ---

class ComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.decision_points = 0

    def visit_If(self, node):
        self.decision_points += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.decision_points += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.decision_points += 1
        self.generic_visit(node)

    def visit_Try(self, node):
        self.decision_points += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):  # Handles 'and' / 'or'
        if isinstance(node.op, (ast.And, ast.Or)):
            self.decision_points += len(node.values) - 1
        self.generic_visit(node)

def calculate_cyclomatic_complexity(source_code):
    tree = ast.parse(source_code)
    analyzer = ComplexityAnalyzer()
    analyzer.visit(tree)
    cc = analyzer.decision_points + 1
    return cc

# --- Sample Function to Analyze ---
sample_code = """
def sample_function(x):
    if x > 0:
        print("Positive")
    elif x == 0:
        print("Zero")
    else:
        print("Negative")

    for i in range(5):
        if i % 2 == 0:
            print("Even")

    while x < 10:
        x += 1
"""

# --- Calculate and Show Result ---
cc = calculate_cyclomatic_complexity(sample_code)
print("📊 McCabe's Cyclomatic Complexity Analysis")
print("Function: sample_function")
print(f"Decision Points Found: {cc - 1}")
print(f"🧮 Cyclomatic Complexity: {cc}")






###############################################################################################################################################################
"""# Unit Testing"""

import unittest

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.acc = BankAccount(100)

    def test_deposit_valid(self):
        """✅ Deposit Positive Amount"""
        self.assertTrue(self.acc.deposit(50))
        self.assertEqual(self.acc.get_balance(), 150)

    def test_deposit_invalid(self):
        """❌ Deposit Negative Amount"""
        self.assertFalse(self.acc.deposit(-10))
        self.assertEqual(self.acc.get_balance(), 100)

    def test_withdraw_valid(self):
        """✅ Withdraw Valid Amount"""
        self.assertTrue(self.acc.withdraw(60))
        self.assertEqual(self.acc.get_balance(), 40)

    def test_withdraw_exceeds_balance(self):
        """❌ Withdraw More Than Balance"""
        self.assertFalse(self.acc.withdraw(200))
        self.assertEqual(self.acc.get_balance(), 100)

    def test_withdraw_negative(self):
        """❌ Withdraw Negative Amount"""
        self.assertFalse(self.acc.withdraw(-30))
        self.assertEqual(self.acc.get_balance(), 100)


if __name__ == "__main__":
    print("\n🔬 Running Unit Tests for BankAccount...\n")
    # Use exit=False to prevent unittest.main from exiting the notebook
    #unittest.main(verbosity=2)
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)












###############################################################################################################################################################
"""# COCOMO cost estimation using function point matrix"""

# COCOMO cost estimation using function point matrix


def calculate_cost(matrix):
	print("Enter DOF between 0 to 6:")
	lines = '''1. Requirement for reliable backup and recovery =
	2. Requirement for data communication =
	3. Extent of distributed processing =
	4. Performance requirements =
	5. Expected operational enviornment =
	6. Extent of online data entries =
	7. Extent of multi-screen or multioperation online data input =
	8. Extent of online updating of master files =
	9. Extent of complex inputs outputs online queries and files =
	10. Extent of complex data processing =
	11. Extent that currently developed code can be designed for reuse =
	12. Extent of conversion and installation included in the design =
	13. Extent of multiple installations in an organization and variety of customer organizations =
	14. Extent of change and focused on ease of use = '''.split("\n")
	dof = []
	for line in lines:
		dof.append(int(input(line)))
	UFP = (matrix[0]*4)+(matrix[1]*5)+(matrix[2]*4)+(matrix[3]*10)+(matrix[4]*7)
	TCF = 0.65 + (0.01*sum(dof))
	return round(UFP * TCF)

# driving code
if __name__ == "__main__":
	prompts = ["inputs", "outputs", "inquiries", "files", "interfaces"]
	inputs = [int(input(f"{prompts[i]} = ")) for i in range(5)]
	cost = calculate_cost(inputs)
	print(f'Estimated Cost: {cost} months')










###############################################################################################################################################################
"""# COCOMO cost estimation using function point matrix grap plot"""

# COCOMO cost estimation using function point matrix

import matplotlib.pyplot as plt

def calculate_cost(matrix, fix):
	dof = [fix for _ in range(14)]	# taking fix values btw [0,6]
	UFP = (matrix[0]*4)+(matrix[1]*5)+(matrix[2]*4)+(matrix[3]*10)+(matrix[4]*7)
	TCF = 0.65 + (0.01*sum(dof))
	return round(UFP * TCF)

if __name__ == "__main__":
	prompts = ["inputs", "outputs", "inquiries", "files", "interfaces"]
	cost = list()
	for i in range(10000):
		cost.append(calculate_cost([i,5,5,5,5], 3))	# for change in value1

	plt.plot(list(range(10000)), cost)
	plt.xlabel("inputs")
	plt.ylabel("cost")
	plt.title("inputs vs cost")
	plt.show()

# this algorithm is linear, so changing any value from the prompts does not make any changes in the resultant plot
# for this reason, only chage in value 1 has shown










###############################################################################################################################################################
"""# **Detect NO. of loop conditions and statements**"""

# Detect NO. of loop conditions and statements

def detect(filename):
    count = {       # counters
        "for": 0,
        "while": 0,
        "if": 0,
        "elif": 0,
        "else": 0,
        "with": 0,
        "case": 0
    }
    with open(filename, "r") as file:
        lines = file.read().split("\n")
        for line in lines:
            tokens = line.strip().split(" ")
            try:
                count[tokens[0]] += 1
            except:
                continue
    return count

# driving code
if __name__ == "__main__":
    counts = detect(input("Enter filename: "))
    print(counts)









###############################################################################################################################################################
"""---

# $$$$$$$

# Acceptance Testing
"""

# Acceptance Testing Example
def place_order(item, quantity):
    if item and quantity > 0:
        return "Order Placed"
    return "Order Failed"

def acceptance_test():
    print("📋 Running Acceptance Test...")
    assert place_order("Laptop", 2) == "Order Placed"
    assert place_order("", 2) == "Order Failed"
    print("✅ Acceptance test passed.")

if __name__ == "__main__":
    acceptance_test()








###############################################################################################################################################################
"""# Alpha Testing"""

# Alpha Testing Simulation
def product_feature():
    return "This is a new feature for internal test."

def alpha_test():
    print("🧪 Running Alpha Test...")
    output = product_feature()
    assert "internal" in output
    print(f"Output: {output}")
    print("✅ Alpha Test Passed.")

if __name__ == "__main__":
    alpha_test()








###############################################################################################################################################################
"""# Beta Testing"""

# Beta Testing Simulation
def feedback_from_user():
    return {"bug": False, "comment": "Works fine!"}

def beta_test():
    print("🌍 Running Beta Test (simulated user)...")
    feedback = feedback_from_user()
    if feedback["bug"]:
        print("❌ Bug reported by user.")
    else:
        print(f"✅ No bugs. User said: {feedback['comment']}")

if __name__ == "__main__":
    beta_test()







###############################################################################################################################################################
"""# Load Testing"""

# Load Testing Simulation
import time

def simulate_login():
    return "Logged In"

def load_test():
    print("💪 Load Testing: Simulating 100 logins")
    start = time.time()
    for _ in range(100):
        assert simulate_login() == "Logged In"
    end = time.time()
    print(f"✅ All logins successful. Time taken: {end - start:.2f} seconds")

if __name__ == "__main__":
    load_test()







###############################################################################################################################################################
"""# Regression Testing"""

# Regression Testing Example
def calculate_total(price, quantity):
    return price * quantity

def test_regression():
    print("🔁 Starting Regression Testing...")
    assert calculate_total(10, 2) == 20
    assert calculate_total(5, 0) == 0
    assert calculate_total(7, 3) == 21
    print("✅ All regression test cases passed.")

if __name__ == "__main__":
    test_regression()






###############################################################################################################################################################
"""# Sanity Testing"""

# Sanity Testing Example
def is_even(num):
    return num % 2 == 0

def sanity_test():
    print("🧠 Running Sanity Test...")
    assert is_even(2) == True
    assert is_even(5) == False
    print("✅ Sanity Test Passed.")

if __name__ == "__main__":
    sanity_test()








###############################################################################################################################################################
"""# Smoke Testing"""

# Smoke Testing Example
def login(username, password):
    if username == "admin" and password == "admin123":
        return True
    return False

def smoke_test():
    print("🔥 Running Smoke Test...")
    try:
        result = login("admin", "admin123")
        assert result == True
        print("✅ Smoke Test Passed.")
    except Exception as e:
        print("❌ Smoke Test Failed.", e)

if __name__ == "__main__":
    smoke_test()








###############################################################################################################################################################
"""# **MOST IMOORTANT**"""

# generate_40KLOC.py    - Organic Input

dummy_line = "print('This is a dummy line of code')\n"
with open("sample_40KLOC.py", "w") as f:
    for _ in range(40_000):
        f.write(dummy_line)

#--------------------------------------------------------------
# generate_100KLOC.py   - Semi - Detached Input

dummy_line = "print('This is a dummy line of code')\n"
with open("sample_100KLOC.py", "w") as f:
    for _ in range(100_000):
        f.write(dummy_line)

#---------------------------------------------------------------
# generate_400KLOC.py  -  Embedded Input

dummy_line = "print('This is a dummy line of code')\n"
with open("sample_400KLOC.py", "w") as f:
    for _ in range(400_000):
        f.write(dummy_line)






###############################################################################################################################################################
# This file is Input for Loop Counting program "Detect NO. of loop conditions and statements"


#save this as demo.py and feed the path to the loop counting program "Detect NO. of loop conditions and statements"
def Demo(arg):
	''' this is a simple code snippet
	sometime there can have multiline comment '''
	# print the argument value
	print(arg)

# driving code
if __name__   ==   "__main__":
	# dummy values
	dummy = [1,2,3]

	for a in dummy:
		Demo(a)
	# end of the code
