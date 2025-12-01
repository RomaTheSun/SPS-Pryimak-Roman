def sub():
    horizontal = 0
    depth = 0

    commands = []
    while True:
        try:
            line = input().strip()
            if not line:
                break
            commands.append(line)
        except EOFError:
            break

    for line in commands:
        direction, value = line.split()
        value = int(value)

        if direction == "forward":
            horizontal += value
        elif direction == "down":
            depth += value
        elif direction == "up":
            depth -= value
    print(horizontal * depth)


def aim():
    horizontal = 0
    depth = 0
    aim = 0

    while True:
        try:
            line = input().strip()
            if not line:
                break

            direction, value = line.split()
            value = int(value)

            if direction == "forward":
                horizontal += value
                depth += aim * value
            elif direction == "down":
                aim += value
            elif direction == "up":
                aim -= value

        except EOFError:
            break

    print(horizontal * depth)

if __name__ == '__main__':
    aim()