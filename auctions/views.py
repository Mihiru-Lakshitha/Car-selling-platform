from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, AuctionListing, Bid, Comment
from .forms import AuctionListingForm, CommentForm


def index(request):
    return render(request, "auctions/index.html", {
        "listings": AuctionListing.objects.all().order_by('-created_at')
    })

def user_profile(request):
    return render(request, 'auctions/user.html') 

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        phone = request.POST["PhoneNo"]
        zip = request.POST["zipcode"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email=email, password=password, phone = phone , zip = zip)
            user.save()

        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,  "auctions/login.html")


# ======================================================================================================================
@login_required(login_url='auctions/login.html')
def create(request):
    return render(request, "auctions/create.html", {
        'form': AuctionListingForm()
    })


@login_required(login_url='auctions/login.html')
def insert(request):
    form = AuctionListingForm(request.POST)
    if form.is_valid():
        auction = AuctionListing(user=request.user, **form.cleaned_data)
        auction.save()
        starting_bid = auction.starting_bid
        bid = Bid(amount=starting_bid, user=request.user, auction=auction)
        bid.save()
        print("auction:" + auction.image_url)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'auctions/create.html', {
            'form': form,
            'error': form.errors
        })


def listing(request, id):
    current = AuctionListing.objects.get(pk=id)
    bid = get_object_or_404(Bid, auction=current)
    comments = Comment.objects.filter(auction=current)
    print("here:" + AuctionListing.objects.get(pk=id).image_url)
    return render(request, 'auctions/listing.html', {
        'auction': current,
        'user': request.user,
        'bid': bid,
        'comments': comments,
        'comment_form': CommentForm()
    })


@login_required(login_url='auctions/login.html')
def update_bid(request, id):
    amount = request.POST['bid']
    if amount:
        amount = float(amount)
        auction = get_object_or_404(AuctionListing, id=id)
        if amount > get_object_or_404(Bid, id=id).amount:
            bid = get_object_or_404(Bid, id=id)
            bid.user, bid.amount = request.user, amount
            bid.save()
            auction.bid_counter += 1
            auction.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            raise ValidationError('Bid must be greater than current Bid value')
    else:
        raise ValidationError('Bid must be greater than current Bid value')


@login_required(login_url='auctions/login.html')
def close_bid(request, id):
    auction = get_object_or_404(AuctionListing, id=id)
    auction.active, auction.winner = False, request.user.username
    auction.save()
    return HttpResponseRedirect(reverse('index'))


@login_required(login_url='auctions/login.html')
def watchlist(request):
    return render(request, "auctions/watchlist.html", {
        "watchlist": request.user.watchlist.all()
    })


@login_required(login_url='auctions/login.html')
def watch(request, id):
    auction = get_object_or_404(AuctionListing, id=id)
    request.user.watchlist.add(auction)
    request.user.watchlist_counter += 1
    request.user.save()
    return HttpResponseRedirect(reverse('index'))


@login_required(login_url='auctions/login.html')
def unwatch(request, id):
    auction = get_object_or_404(AuctionListing, id=id)
    request.user.watchlist.remove(auction)
    request.user.watchlist_counter -= 1
    request.user.save()
    if '/unwatch/' in request.path:
        return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('wishlist'))


def categories(request):
    return render(request, "auctions/categories.html")


def filter(request):
    q = request.GET['category'].lower()
    return render(request, 'auctions/category.html', {
        'listings': AuctionListing.objects.filter(category=q)
    })


def add_comment(request, id):
    anonymous = User.first_name
    if request.user is not anonymous:
        form = CommentForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            comment = Comment(
                user=request.user,
                auction=get_object_or_404(AuctionListing, id=id),
                **f
            )
            comment.save()
            return HttpResponseRedirect(reverse('listing', kwargs={
                'id': id
            }))
    else:
        return render(request, 'auctions/login.html', {
            'message': 'Must be logged in to be able to comment!'
        })

from django.db import connection
from django.shortcuts import render, redirect

@login_required
def delete_account(request):
    if request.method == 'POST':
        # Optional: Add additional confirmation logic here
        user = request.user
        user.delete()  # Delete the user account
        connection.cursor().execute("DELETE FROM django_migrations;")  # Flush the database
        logout(request)  # Logout the user
        return redirect('index')  # Redirect to the home page after successful deletion

    return render(request, 'index.html')


from django.shortcuts import render, redirect
from .forms import UserProfileUpdateForm

def update_avatar(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileUpdateForm(instance=request.user)
    
    return render(request, 'avatar_update.html', {'form': form})


# auctions/views.py
from django.contrib import messages
from .forms import UpdateUserForm

def update_user_details(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST)
        if form.is_valid():
            # Update user details here
            user = request.user
            user.username = form.cleaned_data['new_name'] or user.username
            user.zip = form.cleaned_data['zip_code'] or user.zip
            user.phone = form.cleaned_data['new_phone_number'] or user.phone
            user.email = form.cleaned_data['new_email'] or user.email
            user.save()

            messages.success(request, 'User details updated successfully.')
            return redirect('user_profile')
    else:
        form = UpdateUserForm()

    return render(request, 'update_user_details.html', {'form': form})



from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from .forms import UpdateUserForm, UpdatePasswordForm

def update_user_password(request):
    if request.method == 'POST':
        form = UpdatePasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            current_password = form.cleaned_data['current_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']

            # Check if the current password is valid
            if not user.check_password(current_password):
                messages.error(request, 'Invalid current password.')
                return redirect('user_profile')

            # Check if the new password and confirmation match
            if new_password != confirm_password:
                messages.error(request, 'New password and confirmation do not match.')
                return redirect('user_profile')

            # Update the user's password
            user.set_password(new_password)
            user.save()

            # Update the session to reflect the password change
            update_session_auth_hash(request, user)

            messages.success(request, 'Password updated successfully.')
            return redirect('user_profile')
    else:
        form = UpdatePasswordForm()

    return render(request, 'user.html', {'password_form': form})

# auctions/views.py


def payment_page(request):
    # Any additional logic you need
    return render(request, 'auctions/Payment page.html')
