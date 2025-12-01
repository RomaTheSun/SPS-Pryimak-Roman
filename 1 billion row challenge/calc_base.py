import time

def calculate_stats_per_station(filepath, max_lines=None):
    stats = {}

    with open(filepath, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if max_lines is not None and i >= max_lines:
                break

            try:
                station, value = line.strip().split(';')
                temp = float(value)
            except ValueError:
                continue

            if station not in stats:
                stats[station] = [temp, temp, temp, 1]
            else:
                min_t, total, max_t, count = stats[station]
                stats[station] = [
                    min(min_t, temp),
                    total + temp,
                    max(max_t, temp),
                    count + 1,
                ]

    sorted_stations = sorted(stats.keys())
    results = []
    for station in sorted_stations:
        min_t, total, max_t, count = stats[station]
        mean = total / count
        results.append(f"{station};{min_t:.1f};{mean:.1f};{max_t:.1f}")

    return results


if __name__ == "__main__":
    filepath = "data/measurements.txt"

    start_time = time.time()

    results = calculate_stats_per_station(filepath, None)

    end_time = time.time()
    elapsed_time = end_time - start_time

    for line in results:
        print(line)

    print(f"\nExecution time: {end_time - start_time:.2f} seconds")

#читає за 4.2