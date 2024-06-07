$(document).ready(function() {
    // Handle navbar function
    $('.navbar-nav>li>a').on('click', function(){
        $('#navbarNavDropdown').collapse('hide');
    });
    // Create board
    $('#createBoard').on('click', function(){
        // Get variable
        const boardTitle = $('#boardTitle').val();
        const boardSeed = $('#boardSeed').val();
        console.log(JSON.stringify({
            name: boardTitle,
            seed: boardSeed
        }));
        // Post request to create board
        $.ajax({
            type: "POST",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            url: "/create-board",
            data: JSON.stringify({
                name: boardTitle,
                seed: boardSeed
            }),
            success: function(response) {
                window.location.href = response.redirect_url;
            }
            // Need to handle errors gracefully
         });
    });
})
