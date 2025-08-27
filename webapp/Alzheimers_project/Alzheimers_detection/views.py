from django.shortcuts import render
import numpy as np
import pickle as pkl

# Create your views here.
def input(request):
    return render(request, "input.html")

def loadFile(filename):
    file = open(filename, "rb")
    obj = pkl.load(file)
    file.close()
    return obj

def predict(request):
    svm_model = loadFile("xgboost_model.pkl")
    svm_numerical = loadFile("xgboost_numerical.pkl")
    gender = request.GET['gender']
    Age = int(request.GET['Age'])
    EDUC=int(request.GET['EDUC'])
    SES=float(request.GET['SES'])
    MMSE=int(request.GET['MMSE'])
    CDR=float(request.GET['CDR'])
    eTIV=int(request.GET['eTIV'])
    nWBV=float(request.GET['nWBV'])
    ASF=float(request.GET['ASF'])
    
    if gender == "F":
          F= 1
          M= 0
         
    else:
         F = 0
         M = 1
        
    data = np.array([[M,F,Age,EDUC,SES,MMSE,CDR,eTIV,nWBV,ASF]])
    
    print(data)
    
    test_data = svm_numerical.transform(data)
    prediction = svm_model.predict(test_data)

    if prediction[0] == 0:
        msg = "Nondemented"
    else:
        msg = "demented"

    return render(request, "predict.html", 
                  {"prediction" : msg})
