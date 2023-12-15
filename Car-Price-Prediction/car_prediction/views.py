from django.shortcuts import render
from .forms import CarInputForm
import joblib
import numpy as np


def predict_price(request):
    if request.method == 'POST':
        form = CarInputForm(request.POST)
        if form.is_valid():
            input_data = form.cleaned_data

            # Load the model using joblib
            try:
                model = joblib.load('car_prediction/car.joblib')
            except FileNotFoundError:
                return render(request, 'error.html', {'error_message': 'Model file not found'})

            # Ensure that the loaded model is a scikit-learn model
            if not hasattr(model, 'predict'):
                return render(request, 'error.html', {'error_message': 'Invalid model loaded'})

            # Convert input data to a NumPy array before making predictions
            input_array = np.array([[input_data['mileage'], input_data['num_owners'], input_data['year'], input_data['starting_bid']]])

            # Make predictions
            price_prediction = model.predict(input_array)

            return render(request, 'input_form.html', {'price_prediction': price_prediction[0]})
    else:
        form = CarInputForm()

    return render(request, 'input_form.html', {'form': form})
