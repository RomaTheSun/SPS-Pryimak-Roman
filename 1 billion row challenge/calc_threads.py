import time
from concurrent.futures import ProcessPoolExecutor

def process_chunk(lines):
    stats = {}
    for line in lines:
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
    return stats


def merge_stats(all_stats):
    merged = {}
    for stats in all_stats:
        for station, (min_t, total, max_t, count) in stats.items():
            if station not in merged:
                merged[station] = [min_t, total, max_t, count]
            else:
                m_min, m_total, m_max, m_count = merged[station]
                merged[station] = [
                    min(m_min, min_t),
                    m_total + total,
                    max(m_max, max_t),
                    m_count + count,
                ]
    return merged


def calculate_stats_per_station(filepath, max_lines=None, workers=4, chunk_size=500_000):
    lines = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if max_lines is not None and i >= max_lines:
                break
            lines.append(line)

    chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

    with ProcessPoolExecutor(max_workers=workers) as executor:
        all_stats = list(executor.map(process_chunk, chunks))

    merged = merge_stats(all_stats)

    results = []
    for station in sorted(merged.keys()):
        min_t, total, max_t, count = merged[station]
        mean = total / count
        results.append(f"{station};{min_t:.1f};{mean:.1f};{max_t:.1f}")
    return results


if __name__ == "__main__":
    filepath = "data/measurements.txt"

    start_time = time.time()

    results = calculate_stats_per_station(filepath, max_lines=10_000_000, workers=8)

    end_time = time.time()
    elapsed_time = end_time - start_time

    for line in results:
        print(line)

    print(f"\nExecution time: {elapsed_time:.2f} seconds")


#читає на 2.8