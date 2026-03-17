from collections import deque

def add(queue, name):
    queue.append(name)

def process(queue):
    if queue:
        return queue.popleft()
    return None

def next(queue):
    if queue:
        return queue[0]
    return None


ticket_queue = deque()
add(ticket_queue, "Alice")
add(ticket_queue, "Bob")
process(ticket_queue)
print(next(ticket_queue))