// Message modal for user feedback

$('#messageModal').on('show.bs.modal', function (event) {
    let button = $(event.relatedTarget);
    let message = button.data('message');
    let modal = $(this);
    modal.find('.modal-body').text(message);

    $('#messageModal').on('click', function () {
        $('#messageModal').modal('hide');
    });
});

