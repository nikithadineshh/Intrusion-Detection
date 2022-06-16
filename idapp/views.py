from django.shortcuts import render
from django.http import HttpResponse
import pickle
import time

# Create your views here.
def home(request):
    return render(request,'index.html')

def result(request):
    if request.method == "POST":
        f1 =  request.POST['f1']
        f2 =  request.POST['f2']
        f3 =  request.POST['f3']
        f4 =  request.POST['f4']
        f5 =  request.POST['f5']
        f6 =  request.POST['f6']
        f7 =  request.POST['f7']
        inp = [[0,0,0,f1,f2,0,0,0,0,0,f3,0,0,0,0,0,0,0,0,0,f4,0,f5,0,0,0,0,0,f6,0]]
        
        f = open('GB.pickle', 'rb')
        clfg = pickle.load(f)

        #start_time = time.time()
        test_pred = clfg.predict(inp)[0]
        print(test_pred)
        if test_pred == "normal":
            return render(request, 'result.html', {'f1':"No", "f2":"None"})
        else:
            return render(request, 'result.html', {'f1':"Yes", "f2":test_pred})
    return render(request, 'result.html')

