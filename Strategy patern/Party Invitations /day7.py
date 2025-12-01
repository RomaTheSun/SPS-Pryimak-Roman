def parse_instructions(lines):
    circuit = {}
    for line in lines:
        if not line.strip():
            continue
        expr, target = line.split(" -> ")
        circuit[target.strip()] = expr.strip().split()
    return circuit


def evaluate(wire, circuit, cache):
    if wire.isdigit():
        return int(wire)
    if wire in cache:
        return cache[wire]
    if wire not in circuit:
        raise KeyError(f"Wire '{wire}' not found in circuit.")

    expr = circuit[wire]

    if len(expr) == 1:
        val = evaluate(expr[0], circuit, cache)
    elif len(expr) == 2:
        op, x = expr
        if op != "NOT":
            raise ValueError(f"Unknown unary operation: {op}")
        val = ~evaluate(x, circuit, cache) & 0xFFFF
    else:
        a, op, b = expr

        def val_of(token):
            return int(token) if token.isdigit() else evaluate(token, circuit, cache)

        if op == "AND":
            val = val_of(a) & val_of(b)
        elif op == "OR":
            val = val_of(a) | val_of(b)
        elif op == "LSHIFT":
            val = (val_of(a) << val_of(b)) & 0xFFFF
        elif op == "RSHIFT":
            val = val_of(a) >> val_of(b)
        else:
            raise ValueError(f"Unknown operation: {op}")

    cache[wire] = val
    return val


def main():
    print("Enter your circuit:")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line.strip():
            break
        lines.append(line)

    circuit = parse_instructions(lines)

    cache = {}
    try:
        a_value = evaluate("a", circuit, cache)
    except KeyError as e:
        print(e)
        return

    print(f"Part 1: {a_value}")

    circuit["b"] = [str(a_value)]
    cache = {}
    new_a = evaluate("a", circuit, cache)
    print(f"Part 2: {new_a}")


if __name__ == "__main__":
    main()
