import sys


def measure_memory_usage(n):
    contest_scores = [i * 10 for i in range(n)]

    memory_bytes = sys.getsizeof(contest_scores)

    return len(contest_scores), memory_bytes


input_sizes = [4, 10, 100, 1000]

print("--- Memory Usage Growth Analysis ---")
print(f"{'Input Size (n)':<15} | {'List Size (Elements)':<22} | {'Memory (Bytes)':<15}")
print("-" * 58)

for n in input_sizes:
    length, mem_bytes = measure_memory_usage(n)
    print(f"{n:<15} | {length:<22} | {mem_bytes:<15}")