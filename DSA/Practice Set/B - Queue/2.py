from collections import deque

def calculate(jobs):
    queue = deque(jobs)
    total_time = 0
    
    while queue:
        job_id, pages = queue.popleft()
        total_time += pages
        
    return total_time

jobs = [(1, 5), (2, 3), (3, 2)]
print(f"{calculate(jobs)} seconds")