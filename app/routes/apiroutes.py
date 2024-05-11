from flask import Blueprint, render_template, request, jsonify
from model.data_handler  import load_by_id, load_data, delete_data, update_data, create_data

api_routes = Blueprint('api_routes', __name__)

# Read all items
@api_routes.route('/api/items', methods=['GET'])
def read_items():
    return jsonify(load_data()), 200

# Read items by count
@api_routes.route('/api/items/<int:items>', methods=['GET'])
def read_items_by_count(items):
    return jsonify(load_data()[:items]), 200

# Read an item
@api_routes.route('/api/item/<int:item_id>', methods=['GET'])
def read_item(item_id):
    if isinstance(item_id, int): item = load_by_id(item_id)
    else: return jsonify({'message': 'Invalid item id'}), 400

    if item != None: return jsonify(item), 200
    else: return jsonify({'message': 'Item not found'}), 404

# Create an item
@api_routes.route('/api/item', methods=['POST'])
def create_item():
    data = request.get_json()

    if data: is_created = create_data(data) 
    else: return jsonify({'message': 'Failed to load data'}), 400


    if is_created: return jsonify(data), 200
    else: return jsonify({'message': 'Failed to create an item'}), 404

# Update an item
@api_routes.route('/api/item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    if data: is_updated =  update_data(item_id, data) 
    else: return jsonify({'message': 'Failed to load data'}), 400

    if is_updated: return jsonify({'message': f'Item updated - {item_id}'}), 200
    else: return jsonify({'message': 'Failed to update an item'}), 404

# Delete an item
@api_routes.route('/api/item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if isinstance(item_id, int): is_deleted = delete_data(item_id)
    else: return jsonify({'message': 'Invalid item id'}), 400

    if is_deleted: return jsonify({'message': f'Item deleted - {item_id}'}), 200
    else: return jsonify({'message': 'Failed to delete an item'}), 404