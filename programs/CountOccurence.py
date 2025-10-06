nums = [2, 2, 1, 1, 1, 2, 2]

solution = None
count = 0

for num in nums:
    if count == 0:
        solution = num  # Initialize the solution with the first element

    if solution == num:
        count += 1
    else:
        count -= 1
    print(solution, count)

print(solution)