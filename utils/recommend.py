import json

try:
    with open('data/skin_conditions.json', encoding='utf-8') as f:
        json_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading JSON: {e}")
    json_data = []

    
    
def get_recommended_products(condition_query):
    condition_query = condition_query.strip().lower()
    for entry in json_data:
        condition = entry.get("condition", "").strip().lower()
        if condition_query in condition:
            return entry
    return {}
