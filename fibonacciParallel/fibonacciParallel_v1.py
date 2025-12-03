import sys
import math
import concurrent.futures
import multiprocessing


def fib_fast(n, m):

    if n == 0: return 0
    if n == 1: return 1 % m
    if n == 2: return 1 % m

    binary_str = bin(n)[3:]


    a = 1
    b = 1

    for bit in binary_str:

        temp_a = (a * ((b << 1) - a)) % m

        temp_b = (a * a + b * b) % m

        if bit == '1':
            a = temp_b
            b = (temp_a + temp_b) % m
        else:
            a = temp_a
            b = temp_b

    return a


def worker_task(args):
    chunk, Q = args
    results = []
    for val in chunk:
        results.append(fib_fast(val + 1, Q))
    return results

def MAIN(input_file_path):
    try:
        with open(input_file_path, 'r') as f:
            content = f.read().split()

        if not content:
            return []

        iterator = iter(content)
        try:
            N = int(next(iterator))
            Q = int(next(iterator))
        except StopIteration:
            return []

        # Parse toàn bộ N truy vấn vào danh sách
        queries = []
        # Có thể dùng list comprehension nhưng loop an toàn hơn nếu file lỗi
        for _ in range(N):
            try:
                queries.append(int(next(iterator)))
            except StopIteration:
                break

        num_workers = multiprocessing.cpu_count()

        if N < 5000 or num_workers == 1:
            return worker_task((queries, Q))

        chunk_size = math.ceil(N / num_workers)
        chunks = []
        for i in range(0, len(queries), chunk_size):
            chunks.append((queries[i: i + chunk_size], Q))

        final_results = []
        with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
            for res in executor.map(worker_task, chunks):
                final_results.extend(res)

        return final_results

    except Exception:
        return []


# ------------------------------------------------------------------
# PHẦN TEST CỤC BỘ (Không copy phần này vào hệ thống chấm nếu chỉ yêu cầu hàm MAIN)
# ------------------------------------------------------------------
if __name__ == "__main__":
    test_file = "test_input.txt"
    with open(test_file, "w") as f:
        f.write("3 1000000000\n3\n4\n5")

    # Chạy hàm MAIN
    result = MAIN(test_file)
    print("Output:", result)
    # Output mong đợi: [3, 5, 8]