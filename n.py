import time


def measure_double_loop_steps(n):
    steps = 0
    # Simulating a double loop where total operations = n * n
    for i in range(n):
        for j in range(n):
            steps += 1
    return steps


# Input sizes to test
input_sizes = [4, 10, 100, 1000]

print("--- Double Loop Step Growth Analysis ---")
print(f"{'Input Size (n)':<15} | {'Steps Taken (n^2)':<20}")
print("-" * 38)

for n in input_sizes:
    steps = measure_double_loop_steps(n)
    print(f"{n:<15} | {steps:<20}")