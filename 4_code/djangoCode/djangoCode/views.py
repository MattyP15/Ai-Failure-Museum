from urllib import request
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .forms import ArtefactForm
from .models import Artefact
from django.contrib import messages
def homepage(request):
    return render(request, "main.html")

def category(request):
    return render(request, "category.html")

def login(request):
    return render(request, "login.html")










# ==========================================
# CURATOR TOOLS 
# ==========================================



# create_artefact 
# Purpose: for the user to be able to create and upload an artefact
# Method: get input for the fields 
# Returns: redirect to curator dashboard


# to handle the create and upload of the artifact
def create_artefact(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Artefact.objects.create(title=title, description=description)
        return redirect('curator_dashboard')




# curator_dashboard 
# Purpose: provides a view for users (curators) to be able to view all artefacts that are active or archieved, be able to edit, archieve, delete or create new aratefacts, be able to (redirect) to view analystics.
# Method: get a list of both unarchieved and archieved artefacts, then render the dashboard
# Returns: render of the dashboard page with the list of artefacts

def curator_dashboard(request):

        ##dashboard logic here
    active_artefacts = Artefact.objects.filter(is_archived= False)
    archived_aretfacts = Artefact.objects.filter(is_archived = True)

    return render(request, 'curator/dashboard.html', {
        'active_artefacts': active_artefacts,
        'archived_artefacts': archived_aretfacts
    })


# delete_artefact 
# Purpose: for user to be able to delete artefact, thus removing it from any list of artefacts and removing its data. 
# Method: 1. get artefact. 2. delete 3. redirect
# Returns: redirect to curator dashboard.

def delete_artefact(request, pk): 
    try: 
        artefact = get_object_or_404(Artefact, pk=pk)
        artefact.delete()
        messages.success(request, 'artefact deleted successfully')
    except Exception as e:
        messages.error(request, f'error deleting artefact: {e}')
    return redirect('curator_dashboard') 

# archieve_artefact 
# Purpose: for user to be able to mark artefact as archieved, thus removing it from active list of artefacts that visitors see. 
# Method: 1. get artefact. 2. seet is_archieved to true. 3. save, 4. redirect
# Returns: redirect to curator dashboard.

def archive_artefact(request, pk):
    try: 
    
        artefact= get_object_or_404(Artefact, pk=pk)
        artefact.is_archived = True
        artefact.save()
        messages.success(request, 'artefact archived successfully')
    except Exception as e:
        messages.error(request, f'error archiving artefact: {e}')
    return redirect('curator_dashboard')





# analytics-_view 
# Purpose: To provide user view of the analytics
# Method: //
# Returns: render the analytics page

# to angle the analytics view/dashboard.
def analytics_view(request):
    ## analystic dahsboard logic here
    return render(request, 'curator/analytics.html')