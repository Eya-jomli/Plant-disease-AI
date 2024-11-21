from django.shortcuts import render
from django.http import JsonResponse
from .model import predict_image
from . import utils
from django.core.files.storage import default_storage
from django.utils.safestring import mark_safe  

def backoffice_view(request):
    return render(request, 'backoffice.html')  # Adjust path as necessary
    

def dashboard_view(request):
    return render(request, 'indexback.html')  # Adjust path as necessary

# Home page view
def home(request):
    return render(request, 'index.html')

# Predict view
def predict(request):
    if request.method == 'POST':
        try:
            # Fetching the uploaded image from the request
            file = request.FILES['file']
            img = file.read()

            # Use the predict_image function to predict the disease
            prediction = predict_image(img)
            print(prediction)

            # Mark the prediction result as safe to display in HTML
            res = mark_safe(utils.disease_dic[prediction])

            # Render the display template with the result
            return render(request, 'display.html', {'status': 200, 'result': res})

        except Exception as e:
            print(e)  # For debugging purposes
            return render(request, 'index.html', {'status': 500, 'res': "Internal Server Error"})

    return render(request, 'index.html')



