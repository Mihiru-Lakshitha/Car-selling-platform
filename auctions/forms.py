from django import forms


class AuctionListingForm(forms.Form):
    title = forms.CharField(
        label='Title',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Give it a title'
        }
        )
    )
    
    
    category = forms.CharField(
        label='Category',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'autocomplete': 'on',
            'placeholder': 'Category (optional)'
        }
        )
    )
    
    brand = forms.CharField(
        label='Brand',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'autocomplete': 'on',
            'placeholder': 'Category (optional)'
        }
        )
    )
    
    model = forms.CharField(
        label='Model',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'autocomplete': 'on',
            'placeholder': 'Category (optional)'
        }
        )
    )
    # Additional Fields
    edition = forms.CharField(
        label='Edition',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Edition (optional)'
        }
        )
    )
    year = forms.IntegerField(
        label='Year',
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Year (optional)'
        }
        )
    )
    condition = forms.CharField(
        label='Condition',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Condition (optional)'
        }
        )
    )
    no_of_owners = forms.IntegerField(
        label='Number of Owners',
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Number of Owners (optional)'
        }
        )
    )
    transmission = forms.CharField(
        label='Transmission',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Transmission (optional)'
        }
        )
    )
    engine_capacity = forms.DecimalField(
        label='Engine Capacity',
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Engine Capacity (optional)',
            'min': '0.1',
            'max': '999.9',
            'step': '0.1'
        }
        )
    )
    fuel_type = forms.CharField(
        label='Fuel Type',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Fuel Type (optional)'
        }
        )
    )
    weight = forms.DecimalField(
        label='Weight',
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Weight (optional)',
            'min': '1',
            'max': '99999',
            'step': '1'
        }
        )
    )
    mileage = forms.DecimalField(
        label='Mileage',
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Mileage (optional)',
            'min': '0.01',
            'max': '999999.99',
            'step': '0.01'
        }
        )
    )
    district = forms.CharField(
        label='District',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'District (optional)'
        }
        )
    )
    starting_bid = forms.DecimalField(
        label='Starting Bid',
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Starting bid',
            'min': '0.01',
            'max': '99999999999.99',
            'step': '0.01'
        }
        )
    )
    
    image_url = forms.URLField(
        label='Image URL',
        required=False,
        initial='https://user-images.githubusercontent.com/52632898/161646398-6d49eca9-267f-4eab-a5a7-6ba6069d21df.png',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Image URL (optional)',
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
