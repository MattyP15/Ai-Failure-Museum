from urllib import request
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .forms import ExhibitForm
from .models import Exhibit
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

# create_exhibit
# Purpose: for the user to be able to create and upload an exhibit
# Method: get input for the fields 
# Returns: redirect to curator dashboard
def create_exhibit(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        domain = request.POST.get('domain')
        Exhibit.objects.create(title=title, description=description, domian=domain)
        return redirect('curator_dashboard')




# curator_dashboard 
# Purpose: provides a view for users (curators) to be able to view all exhibits that are active or archieved, be able to edit, archieve, delete or create new aratefacts, be able to (redirect) to view analystics.
# Method: get a list of both unarchieved and archieved exhibits, then render the dashboard
# Returns: render of the dashboard page with the list of exhibits

def curator_dashboard(request):

        ##dashboard logic here
    active_exhibits = Exhibit.objects.filter(is_archived= False)
    archived_aretfacts = Exhibit.objects.filter(is_archived = True)

    return render(request, 'curator/dashboard.html', {
        'active_exhibits': active_exhibits,
        'archived_exhibits': archived_aretfacts
    })


# delete_exhibit 
# Purpose: for user to be able to delete exhibit, thus removing it from any list of exhibits and removing its data. 
# Method: 1. get exhibit. 2. delete 3. redirect
# Returns: redirect to curator dashboard.

def delete_exhibit(request, pk): 
    try: 
        exhibit = get_object_or_404(Exhibit, pk=pk)
        exhibit.delete()
        messages.success(request, 'exhibit deleted successfully')
    except Exception as e:
        messages.error(request, f'error deleting exhibit: {e}')
    return redirect('curator_dashboard') 

# archieve_exhibit 
# Purpose: for user to be able to mark exhibit as archieved, thus removing it from active list of exhibits that visitors see. 
# Method: 1. get exhibit. 2. seet is_archieved to true. 3. save, 4. redirect
# Returns: redirect to curator dashboard.

def archive_exhibit(request, pk):
    try: 
    
        exhibit= get_object_or_404(Exhibit, pk=pk)
        exhibit.is_archived = True
        exhibit.save()
        messages.success(request, 'exhibit archived successfully')
    except Exception as e:
        messages.error(request, f'error archiving exhibit: {e}')
    return redirect('curator_dashboard')





# analytics-_view 
# Purpose: To provide user view of the analytics
# Method: //
# Returns: render the analytics page

# to angle the analytics view/dashboard.
def analytics_view(request):
    ## analystic dahsboard logic here
    return render(request, 'curator/analytics.html')