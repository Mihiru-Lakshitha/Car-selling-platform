function toggleDescription(carId) {
    var description = document.getElementById(carId).getElementsByClassName('car-description')[0];
    if (description.style.display === 'none' || description.style.display === '') {
        description.style.display = 'block';
    } else {
        description.style.display = 'none';
    }
}
