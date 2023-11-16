let currentImageIndex = 0;
const images = [
    "https://www.cnet.com/a/img/resize/d44025be0d94fb9865ae024140d5fddf669485e2/hub/2017/06/07/fd580beb-fb7f-4c98-acc0-df4302a8b19b/2017-honda-civic-type-r-vin-01-1.jpg?auto=webp&width=1200",
    "https://www.carscoops.com/wp-content/uploads/2020/02/2020-Honda-Civic-Type-R-105.jpg",
    "https://hips.hearstapps.com/hmg-prod/images/dsc-0269-1590006745.jpg",
    "https://aws-images.carshop.co.uk/FX/20/FX20TCZ/FX20TCZ-used-HONDA-CIVIC-DIESEL-HATCHBACK-16-iDTEC-SR-5dr-diesel-BLUE-2020-XC-M-19.jpg",
    "https://i.i-sgcm.com/cars_used/202008/923680_2b.jpg"
];

function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    updateImage();
}

function prevImage() {
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    updateImage();
}

function updateImage() {
    const imageElement = document.querySelector('.image-container img');
    imageElement.src = images[currentImageIndex];
}

function toggleDetails() {
    const moreDetails = document.getElementById('moreDetails');
    moreDetails.style.display = moreDetails.style.display === 'none' ? 'block' : 'none';
}

function placeBid() {
    const bidAmount = document.getElementById('bidAmount').value;

    if (!isNaN(bidAmount) && bidAmount > 0) {
        alert('Bid placed: Rs.' + bidAmount);
    } else {
        alert('Please enter a valid bid amount.');
    }
}
