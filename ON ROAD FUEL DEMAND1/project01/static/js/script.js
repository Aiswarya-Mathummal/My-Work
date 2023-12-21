$(document).ready(function() {
    $('#priceForm').submit(function(e) {
        e.preventDefault();

        var quantity = $('#quantity').val();

        $.ajax({
            type: 'POST',
            url: '/calculate_price/',  // URL to your Django view
            data: { quantity: quantity },
            success: function(result) {
                $('#result').html('Price: ' + result);
            }
        });
    });
});
