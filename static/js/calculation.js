$(document).ready(function () {
    // Function to update cart details (total price, item count, and grand total)
    function updateCartDetails() {
        var totalPrice = 0;
        var itemCount = 0;

        // Loop through each product in the cart
        $('.cart .product-details').each(function () {
            var quantity = parseInt($(this).siblings('.product-quantity').find('.quantity-input').val());
            var price = parseFloat($(this).siblings('.product-price').text().replace(/[^\d.]/g, ''));
            totalPrice += quantity * price;
            itemCount += quantity;
        });

        // Update total price and item count in the summary section
        $('#total-price-summary').text('₹ ' + totalPrice.toFixed(2));
        $('#item-count').text(itemCount + ' items');

        // Calculate grand total including shipping
        var shippingCharge = parseFloat($('.summary select option:selected').text().replace(/[^\d.]/g, ''));
        var grandTotal = totalPrice + shippingCharge;
        $('#grand-total').text('₹ ' + grandTotal.toFixed(2));
    }

    // Quantity minus button click event
    $('.quantity-minus').click(function (e) {
        e.preventDefault();
        var input = $(this).siblings('.quantity-input');
        var currentValue = parseInt(input.val());
        if (currentValue > 1) {
            input.val(currentValue - 1);
            updateCartDetails();
        }
    });

    // Quantity plus button click event
    $('.quantity-plus').click(function (e) {
        e.preventDefault();
        var input = $(this).siblings('.quantity-input');
        var currentValue = parseInt(input.val());
        input.val(currentValue + 1);
        updateCartDetails();
    });

    // Input quantity change event
    $('.quantity-input').change(function () {
        updateCartDetails();
    });

    // Shipping method change event
    $('.summary select').change(function () {
        updateCartDetails();
    });

    // Initial calculations
    updateCartDetails();
});
