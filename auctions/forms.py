from django import forms


class AuctionListingForm(forms.Form):
    title = forms.CharField(
        label='Title',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Title'
        }
        )
    )
    
    
    category = forms.CharField(
        label='Category',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'autocomplete': 'on',
            'placeholder': 'Category'
        }
        )
    )
    
    brand = forms.CharField(
        label='Brand',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'autocomplete': 'on',
            'placeholder': 'Brand'
        }
        )
    )
    
    model = forms.CharField(
        label='Model',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'autocomplete': 'on',
            'placeholder': 'Model'
        }
        )
    )
    edition = forms.CharField(
        label='Edition',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Edition'
        }
        )
    )
    year = forms.CharField(
        label='Year',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Year'
        }
        )
    )
    condition = forms.CharField(
    label='Condition',
    required=False,
    widget=forms.Select(choices=[
        ('Select condition', 'Select condition'),
        ('Brand new', 'Brand new'),
        ('Recondition', 'Recondition'),
        ('Second Hand', 'Second Hand'),
    ], attrs={
        'class': 'form-control form-group',
    })
)

    no_of_owners = forms.CharField(
        label='Number of Owners',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Number of Owners'
        }
        )
    )
    transmission = forms.CharField(
    label='Transmission',
    required=False,
    widget=forms.Select(choices=[
        ('Select Transmission','Select Transmission'),
        ('Auto', 'Auto'),
        ('Manual', 'Manual'),
        ('Both', 'Both'),
    ],attrs={
        'class': 'form-control form-group',
    })
)
    engine_capacity = forms.CharField(
        label='Engine Capacity',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Engine Capacity',
        }
        )
    )

    fuelType = forms.CharField(
    label='Fuel Type',
    required= False,
    widget=forms.Select(choices=[
    ('Select Fuel Type','Select Fuel Type'),
    ('Petrol', 'Petrol'),
    ('Diesel', 'Diesel'),
    ('Electric', 'Electric'),
    ('Hybrid', 'Hybrid'),
    ],attrs={
        'class': 'form-control form-group',
    })
    )
    weight = forms.CharField(
        label='Weight',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Weight',
        }
        )
    )
    mileage = forms.CharField(
        label='Mileage',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Mileage',
        }
        )
    )
    district = forms.CharField(
        label='District',
        required=False,
        widget=forms.Select(choices=[
        ('Select District','Select District'),
        ('Colombo', 'Colombo'),
        ('Gampaha', 'Gampaha'),
        ('Kalutara', 'Kalutara'),
        ('Kandy', 'Kandy'),
        ('Matale', 'Matale'),
        ('Nuwara Eliya', 'Nuwara Eliya'),
        ('Galle', 'Galle'),
        ('Matara', 'Matara'),
        ('Hambantota', 'Hambantota'),
        ('Jaffna', 'Jaffna'),
        ('Kilinochchi', 'Kilinochchi'),
        ('Mannar', 'Mannar'),
        ('Vavuniya', 'Vavuniya'),
        ('Mullaitivu', 'Mullaitivu'),
        ('Batticaloa', 'Batticaloa'),
        ('Ampara', 'Ampara'),
        ('Trincomalee', 'Trincomalee'),
        ('Kurunegala', 'Kurunegala'),
        ('Puttalam', 'Puttalam'),
        ('Anuradhapura', 'Anuradhapura'),
        ('Polonnaruwa', 'Polonnaruwa'),
        ('Badulla', 'Badulla'),
        ('Moneragala', 'Moneragala'),
        ('Ratnapura', 'Ratnapura'),
        ('Kegalle', 'Kegalle'),
            
        ],attrs={
            'class': 'form-control form-group',
        }
        )
    )
    starting_bid = forms.CharField(
        label='Starting Bid',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Starting bid',
        }
        )
    )
    
    image_url = forms.URLField(
        label='Image URL',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Upload your vehicle image to Google Drive and paste the link',
        }
        )
    )


    def clean_starting_bid(self):
        amount = float(self.cleaned_data.get('starting_bid'))
        if isinstance(amount, float) and amount > 0:
            return amount
        print(amount)
        raise forms.ValidationError('Should be a number larger than zero!')

    def clean_category(self):
        category = self.cleaned_data.get('category')
        return category.lower()


class CommentForm(forms.Form):
    text = forms.CharField(
        label='',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control-md lead form-group',
            'rows': '3',
            'cols': '100'
        }
        )
    )

    def clean_comment(self):
        text = self.cleaned_data.get('text')
        if len(text) > 0:
            return text
        return self.errors
