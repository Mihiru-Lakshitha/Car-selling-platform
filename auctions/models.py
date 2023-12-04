from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    watchlist_counter = models.IntegerField(default=0, blank=True)
    watchlist = models.ManyToManyField('AuctionListing', related_name='watchlist', blank=True)
    phone = models.CharField(max_length=15, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='Guest.png', blank=True)

    def __str__(self):
        return self.username


class AuctionListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    category = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(default='https://images-platform.99static.com/pzfVOCfWSdCWxplUquFVXeUNeZs=/500x500/top/smart/99designs-contests-attachments/28/28767/attachment_28767406')
    bid_counter = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    winner = models.CharField(max_length=100, blank=True, null=True)
    edition = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(blank=True, null=True)
    condition = models.CharField(max_length=100, blank=True)
    no_of_owners = models.IntegerField(blank=True, null=True)
    transmission = models.CharField(max_length=100, blank=True)
    engine_capacity = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    fuel_type = models.CharField(max_length=100, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    mileage = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True) 
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}: by {self.user.username}'


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount} on {self.auction} by {self.user.username}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.text}'
