// JavaScript (script.js)
function toggleDescription(carId) {
    var description = document.getElementById(carId).getElementsByClassName('car-description')[0];
    if (description.style.display === 'none' || description.style.display === '') {
        description.style.display = 'block';
    } else {
        description.style.display = 'none';
    }
}

function showBidForm(carId) {
    var bidForm = document.getElementById(carId).getElementsByClassName('bid-form')[0];
    bidForm.style.display = 'block';
}

function makeBid(carId) {
    var bidAmountInput = document.getElementById(carId).getElementsByClassName('bid-amount')[0];
    var bidAmount = bidAmountInput.value;

    if (bidAmount.trim() === "") {
        alert("Please enter a valid bid amount.");
    } else {
        alert('Bid placed for ' + carId + ' with amount Rs.' + bidAmount);

        // Optionally, you can reset the input field after the bid is submitted
        bidAmountInput.value = "";

        // Hide the bid form after submission
        var bidForm = document.getElementById(carId).getElementsByClassName('bid-form')[0];
        bidForm.style.display = 'none';
    }
}
