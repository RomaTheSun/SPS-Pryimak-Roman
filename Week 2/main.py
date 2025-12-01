total = 0

print("Enter your Puzzle input:")

while True:
    line = input().strip()
    if line == "":
        break

    digits = [c for c in line if c.isdigit()]
    if digits:
        value = int(digits[0] + digits[-1])
        total += value

print("Sum:", total)
