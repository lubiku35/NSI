// Handle deleting item
$('.delete-item').on('submit',function(e) {
    e.preventDefault();
    let itemId = $(this).find('input[name="item-id"]').val();
    
    $.ajax({
        url: '/api/items/' + itemId,
        type: 'DELETE',
        success: function(response) {
            console.log("Item deleted", response);
            $('input[name="item-id"][value="' + itemId + '"]').closest('tr').remove();
        },
        error: function(xhr) {
            console.error("Error deleting item", xhr.responseText);
        }
    });
});