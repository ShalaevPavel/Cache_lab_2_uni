import random
import time

def remove(s, i):
    s[i] = s[-1]
    return s[:-1]

def random_cyclic_permutation(length):
    result = [0] * length
    unused_indexes = [i + 1 for i in range(length - 1)]
    current_index = 0
    for i in range(length - 1):
        r = random.randint(0, len(unused_indexes) - 1)
        next_ind = unused_indexes[r]
        unused_indexes = remove(unused_indexes, r)
        result[current_index] = next_ind
        current_index = next_ind
    return result

def benchmark_latency(size_bytes, iterations):
    array = random_cyclic_permutation(size_bytes // 4)
    pointer = 0
    start = time.monotonic_ns()
    for i in range(iterations):
        pointer = array[pointer]
    return (time.monotonic_ns() - start) / iterations

if __name__ == '__main__':
    i = 5000

    while i <= 20000000:
        with open("data.txt", "a") as f:
            f.write(str(i) + " " + str(benchmark_latency(i, 100000000)) + "\n")
        i = int(i * 1.2)
