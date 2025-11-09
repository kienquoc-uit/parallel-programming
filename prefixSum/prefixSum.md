# Prefix sum

### **Mã giả:**

```python
function preSum(A, L, R, preSumDict):
		if (L, R) in preSumDict:
        return preSumDict[(L, R)]
        
    if not (1 <= L <= R <= lenght(A)):
        return null
    
    if (L == R):
        preSumDict[(L, L)] = A[L]
        return A[L]
    
    mid = (L + R) / 2
    leftSum = fork Sum(A, L, mid, preSumDict)
    rightSum = fork Sum(A, mid + 1, R, preSumDict)

    join leftSum and rightSum

    sumLR = leftSum + rightSum
    preSumDict[(L, R)] = sumLR
    return sumLR

function prefixSum(A, L, R, offset, preSumDict):
    if not (1 <= L <= R <= lenght(A)):
        return
    
    if (L == R):
        prefixSumArray[L] = A[L] + offset
        return
    
    mid = (L + R) / 2
    leftSum = preSumDict[(L, mid)]

    leftPrefixSum = fork prefixSum(A, L, mid, offset, preSumDict)
    rightPrefixSum = fork prefixSum(A, mid + 1, R, offset + leftSum, preSumDict)

    join leftPrefixSum and rightPrefixSum
```

### Giải thích:

```python
function preSum(A, L, R, preSumDict):
		if (L, R) in preSumDict:
        return preSumDict[(L, R)]
        
    if not (1 <= L <= R <= lenght(A)):
        return null
    
    if (L == R):
        preSumDict[(L, L)] = A[L]
        return A[L]
    
    mid = (L + R) / 2
    leftSum = fork Sum(A, L, mid, preSumDict)
    rightSum = fork Sum(A, mid + 1, R, preSumDict)

    join leftSum and rightSum

    sumLR = leftSum + rightSum
    preSumDict[(L, R)] = sumLR
    return sumLR
```

**preSum(A, L, R, preSumDict):**

- Kiểm tra xem cặp key (L, R) đã có ở trong preSumDict
    
    → Nếu chưa có thì thực hiện tiếp logic tiếp theo
    
    → Nếu có rồi thì trả về kết quả đã lưu trong preSumDict
    
- Hàm có chức năng tính tổng các phần tử của mảng **A trong** đoạn từ **[L, R] và** lưu kết quả vào từ điển **preSumDict**.
- Kiểm tra điều kiện **1 ≤ L ≤ R ≤ length(A)** để đảm L ≤ R và luôn nằm trong khoảng hợp lệ của mảng A (mảng A bắt đầu từ 1)
- Kiểm tra **L == R** không, nếu L == R thì mảng A chỉ có một phần tử ⇒ trả về giá trị của phần tử đó **A[L]** và preSumDict = A[L]
- **mid = (L + R)/2**: tìm điểm chính giữa của đoạn [L, R] (Bước này là chia)
    
    để chia tiếp bài toán thành 2 bài toán con:
    
    → Nửa trái từ L → mid
    
    → Nửa phải từ mid + 1 → R
    
- leftSum và rightSum (Bước này để trị - Thực hiện song song):
    
    Sum(…) là gọi đệ quy lại hàm prefixSum để thực hiện song song tiếp mảng [L, mid] và [mid + 1, right]
    
    fork đánh dấu là thực hiện song song
    
    → leftSum và rightSum được thực hiện cùng lúc
    
- join leftSum and rightSum (Bước Đồng bộ hóa)
    
    Hàm cha (đã chạy xong xong 2 hàm con) không thể tiếp tục chạy cho đến khi cả 2 hàm cong chạy xong
    
    Lệnh join sẽ chờ cho đến khi leftSum và rightSum hoành thành
    
- sumLR = leftSum + rightSum (Bước tổng hợp)
    
    Khi đã có kết quả của hai nửa → cộng lại để có được tổng cho đoạn [L, R]
    
- preSumDict[(L, R)] = sumLR (Bước lưu kết quả)
    
    Lưu lại kết quả vừa tính được (sumLR) vào preSumDict với key là (L, R)
    
    Dùng cho chương trình nếu cần tính toán lại của đoạn [L, R], thì không cần thực hiện lại quá trình fork → join → combine. Chỉ cần lấy kết quả từ preSumDict.
    
- return sum LR
    
    Trả về tổng của hàm đã gọi nó. Kết quả dùng được để tính lại sumLR ở hàm cha