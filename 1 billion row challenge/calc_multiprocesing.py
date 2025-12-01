import time
from concurrent.futures import ProcessPoolExecutor
from itertools import islice


def process_chunk(lines):
    """Обробляє шматок рядків і повертає часткову статистику."""
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
    """Об’єднує статистику з усіх процесів."""
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


def read_in_chunks(file, chunk_size, max_lines=None):
    """Генерує шматки рядків з файлу без завантаження всього у пам’ять."""
    while True:
        if max_lines is not None and max_lines <= 0:
            break
        lines = list(islice(file, chunk_size if max_lines is None else min(chunk_size, max_lines)))
        if not lines:
            break
        if max_lines is not None:
            max_lines -= len(lines)
        yield lines


def calculate_stats_multiprocess(filepath, workers=4, chunk_size=500_000, max_lines=None):
    """Основна функція паралельної обробки файлу."""
    with open(filepath, 'r', encoding='utf-8') as file:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = []
            for chunk in read_in_chunks(file, chunk_size, max_lines):
                futures.append(executor.submit(process_chunk, chunk))

            all_stats = [f.result() for f in futures]

    merged = merge_stats(all_stats)
    return merged


if __name__ == "__main__":
    filepath = "data/measurements.txt"
    start_time = time.time()

    # можна регулювати кількість рядків і процесів
    results = calculate_stats_multiprocess(filepath, workers=8, chunk_size=400_000, max_lines=None)

    elapsed_time = time.time() - start_time

    for station in sorted(results.keys()):
        min_t, total, max_t, count = results[station]
        mean = total / count
        print(f"{station};{min_t:.1f};{mean:.1f};{max_t:.1f}")

    print(f"\nExecution time: {elapsed_time:.2f} seconds")

#читає 10млн за 2.6
#весь файл за 48.5