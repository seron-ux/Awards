from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
# Create your views here.
def index(request):
    return render(request,'index.html',)


def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        procForm=profileForm(request.POST, request.FILES)
        if form.is_valid() and procForm.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            profile=procForm.save(commit=False)
            profile.user=user
            profile.save()

   
        return redirect('login')
    else:
        form= RegistrationForm()
        prof=profileForm()
    params={
        'form':form,
        'profForm': prof
    }
    return render(request, 'users/register.html', params)


def searchprofile(request):
    if 'searchUser' in request.GET and request.GET['searchUser']:
        name = request.GET.get("searchUser")
        searchResults = Projects.search_projects(name)
        message = f'name'
        params = {
            'results': searchResults,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any profile"
    return render(request, 'search.html', {'message': message})


@login_required(login_url='login')   
def addProject(request):
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = projectForm(request.POST,request.FILES)
        if form.is_valid:
            newProj = form.save(commit = False)
            newProj.user = user_profile
            newProj.save()
        return redirect('home')  
    else:
        form = projectForm()
    return render(request,'newProject.html',{'form':form})    

def profile(request,id):
    prof = Profile.objects.get(user = id)
    return render(request,'profile.html',{"profile":prof})


def editprofile(request):
    user= request.user
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.id)
    else:
        user_form = UserUpdateForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'editprofile.html', params)


