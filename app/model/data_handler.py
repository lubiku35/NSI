import json

file = 'measurement-values.json'

def load_data():
    with open('data/' + file, 'r') as f:
        data = json.load(f)
    return data

def load_by_items(items):
    data = load_data()
    return data[:items]

def save_data(data):
    with open('data/' + file, 'w') as f:
        json.dump(data, f, indent=4)

def delete_data(item_id):
    data = load_data()
    
    # Find Item 
    item_to_delete = next((item for item in data if item['id'] == item_id), None)
    
    # If item not found return False
    if item_to_delete is None: return False
    else:
        data = [item for item in data if item['id'] != item_id]
        save_data(data)
        return True

def calculate_average(data):
    sum = 0
    for item in data: sum += item['temp']
    return sum / len(data)