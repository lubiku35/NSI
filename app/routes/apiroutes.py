from flask import Blueprint, render_template, request, jsonify

from model.data_handler  import delete_data

api_routes = Blueprint('api_routes', __name__)

# Create an item
@api_routes.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if data:
        return jsonify(data), 200
    else:
        return jsonify({'message': 'Failed to create an item'}), 400

# Read all items
@api_routes.route('/api/items', methods=['GET'])
def read_items():
    return jsonify({'message': 'Read all items'}), 200

# Read an item
@api_routes.route('/api/item/<int:item_id>', methods=['GET'])
def read_item(item_id):
    return jsonify({'message': 'Read an item'}), 200

# Update an item
@api_routes.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    if data:
        return jsonify(data), 200
    else:
        return jsonify({'message': 'Failed to update an item'}), 400

# Delete an item
@api_routes.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    is_deleted = delete_data(item_id)
    if is_deleted: return jsonify({'message': 'Item deleted'}), 200
    else: return jsonify({'message': 'Failed to delete an item'}), 404