n = 4

print("=== Welcome to the Contest Points Challenge! ===")
print("Scenario: Student 1 earns 1 pt, Student 2 earns 2 pts, up to Student 4.")
guess = input("Your guess - Total points: 1 + 2 + 3 + 4 = ")

input("\nFormula: one calculation. Press Enter to run ")
total_formula = n * (n + 1) // 2
print(f" total = {total_formula}  steps = 1")


input(
    "\nLoop: adds one student at a time. Press Enter to run "
)  #
total_loop = 0
steps_loop = 0
for student in range(1, n + 1):
    total_loop += student
    steps_loop += 1
print(f" total = {total_loop}  steps = {steps_loop}")

input(
    "\nDouble Loop: counts every single point. Press Enter to run "
)  
total_double = 0
steps_double = 0
for student in range(1, n + 1):
    for point in range(1, student + 1):
        total_double += 1
        steps_double += 1
print(f" total = {total_double}  steps = {steps_double}")

print("\n=== Analysis Complete ===")