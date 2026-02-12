from urllib import request
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ArtefactForm

def homepage(request):
    return render(request, "main.html")

def category(request):
    return render(request, "category.html")

def login(request):
    return render(request, "login.html")










# ==========================================
# CURATOR TOOLS 
# ==========================================



# to handle the upload of the artifact
def upload_artefact(request):
    
  """   if request.method == "POST": 
        form ArtefactForm(request.POST, request.FILES)
        
        if form.is_valid(): 
            form.save()
            return redirect('cureator_dashboard') #wehen successfully uploaded, redirect back to dashboard
    else:
        form = ArtefactForm() """
  return render(request, 'curator/upload.html', {'form': form})




# to handle the curator dashboard

def curator_dashboard(request):
    ##dashboard logic here

    return render(request, 'curator/dashboard.html')


# to angle the analytics view/dashboard.
def analytics_view(request):
    ## analystic dahsboard logic here
    return render(request, 'curator/analytics.html')