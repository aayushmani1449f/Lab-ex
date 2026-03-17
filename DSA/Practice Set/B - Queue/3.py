from collections import deque

def sliding_window(arr, k):
    dq = deque()
    result = []
    
    for i in range(len(arr)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()
            
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
            
        dq.append(i)
        
        if i >= k - 1:
            result.append(arr[dq[0]])
            
    return result

arr = [4, 3, 5, 2, 1, 6, 7]
k = 3
print(sliding_window(arr, k))