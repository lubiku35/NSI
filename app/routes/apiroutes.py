from flask import Blueprint, render_template, request, jsonify

from model.data_handler  import delete_data

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    is_deleted = delete_data(item_id)
    if is_deleted: return jsonify({'message': 'Item deleted'}), 200
    else: return jsonify({'message': 'Failed to delete an item'}), 404