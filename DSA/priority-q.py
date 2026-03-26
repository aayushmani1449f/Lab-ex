import heapq

pq = []

heapq.heappush(pq, 1)
heapq.heappush(pq, 8)
heapq.heappush(pq, 5)

while pq:
    print(heapq.heappop(pq))