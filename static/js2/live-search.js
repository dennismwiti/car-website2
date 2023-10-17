// live-search.js

$(document).ready(function () {
    $('#live-search-form').on('submit', function (e) {
        e.preventDefault(); // Prevent the form from submitting

        var query = $('#search-input').val();

        // Perform AJAX request to your backend
        $.ajax({
            type: 'GET',
            url: '/search/',  // Replace with the actual URL for your search endpoint
            data: { q: query },
            success: function (data) {
                // Update the search results div with the response from the server
                $('#search-results').html(data);
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    });

    // Trigger live search on keyup event
    $('#search-input').on('keyup', function () {
        $('#live-search-form').submit();
    });
});
