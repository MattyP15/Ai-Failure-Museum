from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ArtefactForm

def homepage(request):
    return render(request, "main.html")

def category(request):
    return render(request, "category.html")

def login(request):
    return render(request, "login.html")

# to handle the upload of the artifact
def upload_artefact(request):
    if request.method == "POST": 
        form ArtefactForm(request.POST, request.FILES)
        
        if form.is_valid(): 
            form.save()
            return redirect('cureator_dashboard') #wehen successfully uploaded, redirect back to dashboard
    else:
        form = ArtefactForm()
    return render(request, 'upload.html', {'form' : form})