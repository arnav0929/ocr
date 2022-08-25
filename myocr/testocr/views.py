from django.shortcuts import render, HttpResponse, redirect
from subprocess import run, PIPE
import sys

# Create your views here.
def index(request):
    if request.method == 'POST':   
        print(1)     
        run([sys.executable, 'testocr/_main.py'],
            shell=False, stdout=PIPE)

    return render(request,'index.html')