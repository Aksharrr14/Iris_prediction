from django.shortcuts import render
from django.http import JsonResponse
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import os
from django.conf import settings

# Create your views here.

def predict(request):
    return render(request, 'predict.html')

def predict_chances(request):
    print("hi")
    if request.method == 'POST' and request.POST.get('action') == 'post':
        try:
            print("idhar aaraha")
            # Receiving data from the client
            sepal_length = float(request.POST.get('sepal_length'))
            sepal_width = float(request.POST.get('sepal_width'))
            petal_length = float(request.POST.get('petal_length'))
            petal_width = float(request.POST.get('petal_width'))

            # Load the dataset
            dataset_path = os.path.join(settings.BASE_DIR, 'Iris.csv')  # Update path
            dataset = pd.read_csv(dataset_path)
            print(dataset.head)
            
            
            # Train the model
            X = dataset[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
            y = dataset['Species']
           
            model = GaussianNB()
            model.fit(X, y)

            # Predict classification for input features
            result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
            classification = result[0]

            # Send back the result as JSON
            return JsonResponse({
                'result': classification,
                'sepal_length': sepal_length,
                'sepal_width': sepal_width,
                'petal_length': petal_length,
                'petal_width': petal_width
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method or action'})
