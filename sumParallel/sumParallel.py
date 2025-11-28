import multiprocessing
import concurrent.futures


def chunk_list(data, num_chunks):
    avg = len(data) / float(num_chunks)
    out = []
    last = 0.0

    while last < len(data):
        out.append(data[int(last):int(last + avg)])
        last += avg
    return out


def worker_sum(sub_array):
    return sum(sub_array)


def MAIN(A):
    try:
        num_workers = multiprocessing.cpu_count()
    except NotImplementedError:
        num_workers = 2

    chunks = chunk_list(A, num_workers)
    total_sum_par = 0

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
        results = executor.map(worker_sum, chunks)

        for res in results:
            total_sum_par += res

    return total_sum_par
