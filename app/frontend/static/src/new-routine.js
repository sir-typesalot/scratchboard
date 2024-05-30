
$('#addExercise').on('click', function(){
    var exName = $('#exName').val();
    var isUnilateral = $('#isUnilateral').is(':checked');
    var isBodyweight = $('#isBodyweight').is(':checked');
    generateExerciseData(exName, isBodyweight, isUnilateral)
});

function generateExerciseData(exName, isBodyweight, isUnilateral) {
    $("#exerciseContainer").append(
        `<div class="exContainer" id="${exName}">
            <div class="row mx-2">
                <input type="text" name="exName" class="form-control" value="${exName}">
            </div>
            <div class="exSets"></div>
            <div class="d-flex mx-2">
                <button class="btn btn-danger ms-auto">Delete</button>
            </div>
        </div>`
    );
};

function generateSetData() {

};
