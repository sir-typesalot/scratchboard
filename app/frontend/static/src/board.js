$(document).ready(function() {
    // Load tasks first thing
    loadTaskData();
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
        const taskStatus = $('#taskStatus').val();
        const taskDescription = $('#taskDescription').val();

        console.log(`${taskTitle} ${taskTag} ${dueDate} ${taskStatus} ${taskDescription}`);
        $.ajax({
            type: "POST",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            url: `${window.location.pathname}/tasks/new`,
            data: JSON.stringify({
                title: taskTitle,
                tag: taskTag,
                dueDate: dueDate,
                status: taskStatus,
                description: taskDescription
            }),
            success: function() {
                location.reload(true);
            }
            // Need to handle errors gracefully
        });
    });
});

// Function to format tasks data that we get from the API into swimlanes
function renderData(data) {
    // Clean out the lanes since we populate them
    $('.swimlane').empty();

    data.forEach(item => {
        let container = $(`#${item.status}-lane`);
        let url = `${window.location.pathname}/tasks/${item.task_id}`;
        container.append(`
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">
                    <a href="${url}">
                        ${item.title}
                    </a>
                </h5>
            </div>
        </div>
        `)
    });
}

function loadTaskData() {
    $.ajax({
        type: "GET",
        dataType: "json",
        url: `${window.location.pathname}/tasks`,
        success: function(response) {
            console.log(response);
            renderData(response.data);
        },
        error: function(xhr, status, error) {
            console.error('AJAX Error:', status, error);
        }
    });
}
