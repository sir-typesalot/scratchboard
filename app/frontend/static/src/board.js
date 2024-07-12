$(document).ready(function() {
    // Load tasks first thing
    loadTaskData();
    loadTagData();

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

//dragula JS
$(function() {
    dragula([
        document.getElementById("todo-lane"),
        document.getElementById("progress-lane"),
        document.getElementById("done-lane")], {
        removeOnSpill: false
})
  .on("drag", function(el) {
    el.className.replace("ex-moved", "");
  })
  .on("drop", function(el) {
    el.className += "ex-moved";
});
});




// Function to format tasks data that we get from the API into swimlanes
function renderTasks(data) {
    // Clean out the lanes since we populate them
    $('.swimlane').empty();

    data.forEach(item => {
        let container = $(`#${item.status}-lane`);
        let url = `${window.location.pathname}/tasks/${item.task_id}`;
        container.append(`
        <li class="card">
            <div class="card-body">
                <h5 class="card-title">
                    <a href="${url}">
                        ${item.title}
                    </a>
                </h5>
            </div>
        </li>
        `)
    });



}

function renderTags(data) {
    data.forEach(item => {
        let containter = $(`#taskTag`);
        let url = `${window.location.pathname}/tags/${item.tag_id}`;
        containter.append(`
        <option value = "${item.tag_name}">${item.tag_name}</option>
        `)
    });
}


function loadTaskData() {
    $.ajax({
        type: "GET",
        dataType: "json",
        url: `${window.location.pathname}/tasks`,
        success: function(response) {
            // console.log(response);
            renderTasks(response.data);
        },
        error: function(xhr, status, error) {
            console.error('AJAX Error:', status, error);
        }
    });
}

function loadTagData() {
    $.ajax({
        type: "GET",
        dataType: "json",
        url: `${window.location.pathname}/tags`,
        success: function(response) {
            // console.log(response);
            renderTags(response);
        },
        error: function(xhr, status, error) {
            console.error('AJAX Error:', status, error);
        }
    });
}