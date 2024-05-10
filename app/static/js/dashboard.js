//Handle get items by number
$('.dropdown-get-item').on('click', function(e) {
    e.preventDefault();
    let numberOfItems = $(this).text();
    $.ajax({
        url: '/api/items/' + numberOfItems,
        type: 'GET',
        success: function(response) {
            console.log(response);
            let tableBody = '';
            response.forEach(function(item) {
                tableBody += '<tr><td>' + item.timestamp + '</td><td>' + item.temp + ' °C</td><td id="action-column"><form class="delete-item" action="" method=""><input type="hidden" name="item-id" value="' + item.id + '"><button type="submit" class="btn btn-danger btn-sm">Delete</button></form><form class="update-item" action="" method=""><button type="button" class="btn btn-warning btn-sm update-item-btn" data-item-id="' + item.id + '" data-item-timestamp="' + item.timestamp + '" data-item-temp="' + item.temp + '" data-toggle="modal" data-target="#updateItemModal">Update</button></form></td></tr>';
            });
            $('.data-table').html(tableBody);
        },
        error: function(xhr) {
            console.error("Error getting items", xhr.responseText);
        }
    });
});

// Handle updating item
$('#updateItemModal').on('show.bs.modal', function(e) {
    let button = $(e.relatedTarget);
    let itemId = button.data('item-id');
    let itemTimestamp = button.data('item-timestamp');
    let itemTemp = button.data('item-temp');
    let modal = $(this);
    modal.find('input[name="id"]').val(itemId);
    modal.find('input[name="timestamp"]').val(itemTimestamp);
    modal.find('input[name="temp"]').val(itemTemp);

    $('#updateItemForm').on('submit', function(e) {
        e.preventDefault();
        let formData = $(this).serializeArray();
        let jsonData = {};
        formData.forEach(function(item) {
            if (item.name === 'temp' || item.name === 'id') { item.value = parseFloat(item.value); }
            jsonData[item.name] = item.value;
        });

        $.ajax({
            url: '/api/item/' + itemId,
            type: 'PUT',
            data: JSON.stringify(jsonData),
            contentType: 'application/json',
            success: function(response) {
                console.log(response);
                let updatedRow = '<td>' + response.timestamp + '</td><td>' + response.temp + ' °C</td><td id="action-column"><form class="delete-item" action="" method=""><input type="hidden" name="item-id" value="' + response.id + '"><button type="submit" class="btn btn-danger btn-sm">Delete</button></form><form class="update-item" action="" method=""><button type="button" class="btn btn-warning btn-sm update-item-btn" data-item-id="' + response.id + '" data-item-timestamp="' + response.timestamp + '" data-item-temp="' + response.temp + '" data-toggle="modal" data-target="#updateItemModal">Update</button></form></td>';
                $('input[name="item-id"][value="' + itemId + '"]').closest('tr').html(updatedRow);
                $('#updateItemModal').modal('hide');
            },
            error: function(xhr) {
                console.error("Error updating item", xhr.responseText);
            }
        });
    });
});

// Handle adding item
$('#dataInsertForm').on('submit', function(e) {
    e.preventDefault();
    let formData = $(this).serializeArray();
    let jsonData = {};
    formData.forEach(function(item) {
        if (item.name === 'temp') { item.value = parseFloat(item.value); }
        jsonData[item.name] = item.value;
    });

    $.ajax({
        url: '/api/item',
        type: 'POST',
        data: JSON.stringify(jsonData),
        contentType: 'application/json',
        success: function(response) {
            console.log(response);
            let newRow = '<tr><td>' + response.timestamp + '</td><td>' + response.temp + ' °C</td><td id="action-column"><form class="delete-item" action="" method=""><input type="hidden" name="item-id" value="' + response.id + '"><button type="submit" class="btn btn-danger btn-sm">Delete</button></form><form class="update-item" action="" method=""><button type="button" class="btn btn-warning btn-sm update-item-btn" data-item-id="' + response.id + '" data-item-timestamp="' + response.timestamp + '" data-item-temp="' + response.temp + '" data-toggle="modal" data-target="#updateItemModal">Update</button></form></td></tr>'; 
            $('.data-table').append(newRow);
        },
        error: function(xhr) {
            console.error("Error adding item", xhr.responseText);
        }
    });
})

// Handle deleting item
$('.delete-item').on('submit',function(e) {
    e.preventDefault();
    let itemId = $(this).find('input[name="item-id"]').val();
    
    $.ajax({
        url: '/api/item/' + itemId,
        type: 'DELETE',
        success: function(response) {
            console.log( response);
            $('input[name="item-id"][value="' + itemId + '"]').closest('tr').remove();
        },
        error: function(xhr) {
            console.error("Error deleting item", xhr.responseText);
        }
    });
});

