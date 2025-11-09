import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager
import numpy as np


def preSum(A, L, R, preSumDict):
    if (L, R) in preSumDict:
        return preSumDict[(L, R)]

    if L > R:
        return 0, preSumDict
    if L == R:
        preSumDict[(L, R)] = A[L]
        return A[L], preSumDict
    mid = (L + R) // 2
    with ProcessPoolExecutor(max_workers=2) as executor:
        left_future = executor.submit(preSum, A, L, mid, preSumDict)
        right_future = executor.submit(preSum, A, mid + 1, R, preSumDict)
        leftSum, _ = left_future.result()
        rightSum, _ = right_future.result()
    preSumDict[(L, R)] = leftSum + rightSum
    return leftSum + rightSum, preSumDict


def prefixSum(A, L, R, offset, preSumDict, prefixSumList):
    if L > R:
        return
    if L == R:
        prefixSumList[L] = int(A[L] + offset)
        return
    mid = (L + R) // 2
    leftSum = preSumDict[(L, mid)]
    with ProcessPoolExecutor(max_workers=2) as executor:
        left_future = executor.submit(prefixSum, A, L, mid, offset, preSumDict, prefixSumList)
        right_future = executor.submit(prefixSum, A, mid + 1, R, offset + leftSum, preSumDict, prefixSumList)
        left_future.result()
        right_future.result()


if __name__ == '__main__':
    mp.set_start_method('spawn', force=True)
    A = np.random.randint(0, 10, size=10)
    print(f"Input array: {A}")

    manager = Manager()
    preSumDict = manager.dict()
    _, preSumDict = preSum(A, 0, len(A) - 1, preSumDict)

    prefixSumList = manager.list([0] * len(A))
    prefixSum(A, 0, len(A) - 1, 0, preSumDict, prefixSumList)

    print(f"Prefix-sum array: {list(prefixSumList)}")
    print(f"preSumDict: {preSumDict}")
    print(f"preSumDict length: {len(preSumDict)}")
