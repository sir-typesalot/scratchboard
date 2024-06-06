$(document).ready(function() {
    // Initialize Select2 with tag creation enabled
    $('#taskModal').on('shown.bs.modal', function(){
        $('#taskTag').select2({
            dropdownParent: $('#taskModal'),
            tags: true,
            placeholder: "Select or add a tag",
            createTag: function(params) {
                var term = $.trim(params.term);
                if (term === '') {
                    return null;
                }
                return {
                    id: term,
                    text: term,
                    newTag: true // add additional parameters
                };
            }
        });

        $('#taskTitle').trigger('focus');
    });

    $('#saveTask').on('click', function(){
        const taskTitle = $('#taskTitle').val();
        const taskTag = $('#taskTag').val();
        const dueDate = $('#dueDate').val();
        const taskCategory = $('#taskCategory').val();
        const taskComments = $('#taskComments').val();

        // Add your logic to save the task here
        // For example, you might use AJAX to send the data to your server

        // Close the modal after saving the task
        $('#taskModal').modal('hide');
    });
});
