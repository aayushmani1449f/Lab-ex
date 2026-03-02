company_tree = {
    "id": 1,
    "name": "Alice CEO",
    "department": "Executive",
    "subordinates": [
        {
            "id": 2,
            "name": "Bob Manager",
            "department": "Engineering",
            "subordinates": [
                {"id": 3, "name": "Charlie", "department": "Engineering", "subordinates": []},
                {"id": 4, "name": "Dave", "department": "QA", "subordinates": []}
            ]
        },
        {
            "id": 5,
            "name": "Eve Manager",
            "department": "Sales",
            "subordinates": [
                {"id": 6, "name": "Frank", "department": "Sales", "subordinates": []}
            ]
        }
    ]
}

def find_department(person, target_id):
    if person.get("id") == target_id:
        return person.get("department")
    
    for subordinate in person.get("subordinates", []):
        found_dept = find_department(subordinate, target_id)
        if found_dept is not None:
            return found_dept
            
    return None

result = find_department(company_tree, 4)
print(result)