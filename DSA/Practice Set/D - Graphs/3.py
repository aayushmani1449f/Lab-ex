from collections import deque

def course_scheduler(courses, prerequisites):
    in_degree = {course: 0 for course in courses}
    graph = {course: [] for course in courses}
    
    for prereq, course in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
        
    queue = deque([course for course in courses if in_degree[course] == 0])
    order = []
    
    while queue:
        current = queue.popleft()
        order.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    if len(order) == len(courses):
        return " ".join(order)
    return "Impossible to complete courses"