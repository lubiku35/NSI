import json, sys
from model import db

def load_data():
    return db.load_data()

def load_by_id(item_id):
    return db.load_data_by_id(item_id)

def load_by_items(items):
    return db.load_data_by_items(items)

def update_data(item_id, new_data):
    # Check ID Value URL and JSON are same and delete json id then
    if 'id' not in new_data: return False
    if item_id != new_data['id']: return False
    del new_data['id']

    # Check Values
    if ('temp' not in new_data) or ('timestamp' not in new_data): return False
    
    # Find Item 
    if db.load_data_by_id(item_id) is None: return False

    # Check Correct Values
    if (not isinstance(new_data['temp'], float)) and (not isinstance(new_data['temp'], int)):  return False
    if (not isinstance(new_data['timestamp'], str)): return False

    # Check if timestamp is in correct format
    try: 
        from datetime import datetime
        datetime.strptime(new_data['timestamp'], '%Y-%m-%d %H:%M:%S')
    except ValueError: return False

    # Update Item
    db.update_data(item_id, new_data)
    return True
        
def create_data(new_data):
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
    if db.create_data(new_data) is False: return False
    return True

def delete_data(item_id):
    # Find Item 
    if db.load_data_by_id(item_id) is None: return False

    # Delete Item
    if db.delete_data(item_id) is False: return False
    return True

def calculate_average(data):
    sum = 0
    if len(data) == 0: return 0
    for item in data: sum += item['temp']
    return sum / len(data)