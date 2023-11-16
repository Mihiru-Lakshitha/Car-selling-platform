
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
        alert("Please enter a bid amount.");
    } else if (isNaN(bidAmount) || parseFloat(bidAmount) <= 0) {
        alert("Please enter a valid bid amount greater than zero.");
    } else {
        alert('Bid placed for ' + carId + ' with amount Rs.' + bidAmount);

       
        bidAmountInput.value = "";

        
        var bidForm = document.getElementById(carId).getElementsByClassName('bid-form')[0];
        bidForm.style.display = 'none';
    }
}
