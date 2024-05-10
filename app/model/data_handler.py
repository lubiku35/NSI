import json, sys

file = 'measurement-values.json'

def load_data():
    with open('data/' + file, 'r') as f: data = json.load(f)
    if data: return data
    else: return []

def load_by_id(item_id):
    data = load_data()
    return next((item for item in data if item['id'] == item_id), None)

def load_by_items(items):
    data = load_data()
    return data[:items]

def save_data(data):
    with open('data/' + file, 'w') as f: json.dump(data, f, indent=4)

def update_data(item_id, new_data):
    data = load_data()
    
    # Check ID Value URL and JSON are same and delete json id then
    if 'id' not in new_data: return False
    if item_id != new_data['id']: return False
    del new_data['id']

    # Check Values
    if ('temp' not in new_data) or ('timestamp' not in new_data): return False
    
    # Find Item 
    item_to_update = next((item for item in data if item['id'] == item_id), None)
    
    # Check Correct Values
    if (not isinstance(new_data['temp'], float)) and (not isinstance(new_data['temp'], int)):  return False
    if (not isinstance(new_data['timestamp'], str)): return False

    # Check if timestamp is in correct format
    try: 
        from datetime import datetime
        datetime.strptime(new_data['timestamp'], '%Y-%m-%d %H:%M:%S')
    except ValueError: return False

    # If item not found return False
    if item_to_update is None: return False
    else:
        item_to_update.update(new_data)
        save_data(data)
        return True
    
def create_data(new_data):
    data = load_data()
    
    # Check Values
    if ('temp' not in new_data) or ('timestamp' not in new_data): return False
    
    # Check Correct Values
    if (not isinstance(new_data['temp'], float)) and (not isinstance(new_data['temp'], int)):  return False
    if (not isinstance(new_data['timestamp'], str)): return False

    # Check if timestamp is in correct format
    try: 
        from datetime import datetime
        datetime.strptime(new_data['timestamp'], '%Y-%m-%d %H:%M:%S')
    except ValueError: return False

    # Add new item
    new_item = {
        'id': data[-1]['id'] + 1 if data else 1,
        'timestamp': new_data['timestamp'],
        'temp': new_data['temp']
    }
    data.append(new_item)
    save_data(data)
    return True


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