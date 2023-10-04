from django.shortcuts import render
from django.shortcuts import render, redirect
import numpy as np
import joblib

model = joblib.load('C:/Users/gsadh/Desktop/PROJECT/CODE/deploy/django deploy without ULI/app/Dt.pkl')

# Create your views here.
def home(request):
    return render(request, "index.html")


def predict(request):
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features)]
        print(final_features)
        prediction = model.predict(final_features)
        print(prediction)
        output = prediction[0]
        if output == 1:
            return render(request, 'index.html', {"prediction_text":"Affected By Lung Cancer"})
        else:
            return render(request, 'index.html', {"prediction_text":"Not Affected By Lung Cancer"})
        print(output)
