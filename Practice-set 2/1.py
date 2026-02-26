fleet_data = [
    {
        "ship_name": "Ocean Quest",
        "containers": [
            {
                "container_id": "OQ-101",
                "items": [
                    {"name": "Large Glass Vase", "is_fragile": True, "destination": "LON", "weight": 12},
                    {"name": "Steel Beams", "is_fragile": False, "destination": "LON", "weight": 500},    
                    {"name": "Antique Mirror", "is_fragile": True, "destination": "NYC", "weight": 15},   
                ]
            }
        ]
    },
    {
        "ship_name": "Sea Empress",
        "containers": [
            {
                "container_id": "SE-205",
                "items": [
                    {"name": "Porcelain Bathtub", "is_fragile": True, "destination": "LON", "weight": 45},
                    {"name": "Crystal Glasses", "is_fragile": True, "destination": "LON", "weight": 5},    
                ]
            }
        ]
    }
]

def extract_fragile_heavy_lon_items(fleet):
    filtered_items = [
        item["name"]                                  
        for ship in fleet                             
        for container in ship["containers"]           
        for item in container["items"]                
        if item.get("is_fragile") == True             
        and item.get("destination") == "LON"          
        and item.get("weight", 0) > 10                
    ]
    
    return filtered_items

result = extract_fragile_heavy_lon_items(fleet_data)
print(result)