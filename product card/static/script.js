function placeBid() {
    const bidAmount = document.getElementById('bidAmount').value;

  
    if (!isNaN(bidAmount) && bidAmount > 0) {
       
        alert('Bid placed: Rs.' + bidAmount);
    } else {
        alert('Please enter a valid bid amount.');
    }
}
