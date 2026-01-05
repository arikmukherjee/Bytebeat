import math
import time

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print("Move disk", n, "from", source, "to", target)
    tower_of_hanoi(n-1, auxiliary, target, source)

if __name__ == "__main__":
    num_disks = int(input("Enter the number of disks: "))
    source_tower = input("Enter the name of the source tower: ")
    target_tower = input("Enter the name of the target tower: ")
    auxiliary_tower = input("Enter the name of the auxiliary tower: ")
    print("Steps to solve the Tower of Hanoi problem:")
    tower_of_hanoi(num_disks, source_tower, target_tower, auxiliary_tower)


# Calculate theoretical time complexity using 2^n
theoretical_time_complexity = math.pow(2, num_disks)

# Measure the actual time taken for the Tower of Hanoi algorithm
start_time = time.time()
tower_of_hanoi(num_disks, source_tower, target_tower, auxiliary_tower)
end_time = time.time()

# Calculate practical time complexity
practical_time_complexity = end_time - start_time

print(f"Theoretical Time Complexity (2^n): {theoretical_time_complexity}")
print(f"Practical Time Complexity: {practical_time_complexity} seconds")
