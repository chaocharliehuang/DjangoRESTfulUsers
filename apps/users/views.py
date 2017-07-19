from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse

from .models import User

def index(request):
    users = User.objects.all()
    context = {"users": []}
    for user in users:
        context['users'].append({
            "id": user.id,
            "full_name": user.first_name + " " + user.last_name,
            "email": user.email,
            "created_at": user.created_at.strftime('%B %e, %Y')
        })
    return render(request, 'users/index.html', context)

def show(request, id):
    if request.method == 'GET':
        id = int(id)
        user = User.objects.get(id=id)
        context = {
            "id": id,
            "full_name": user.first_name + " " + user.last_name,
            "email": user.email,
            "created_at": user.created_at.strftime('%B %e, %Y')
        }
        return render(request, 'users/user.html', context)
    elif request.method == 'POST':
        pass

def new(request):
    return render(request, 'users/new.html')

def create(request):
    if request.method == 'POST':

        # FORM VALIDATION
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('users:new'))

        # ADD TO DATABASE
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        new_user_id = str(User.objects.last().id)
        
        '''ASK KEVIN ABOUT HOW TO REDIRECT HERE'''
        return redirect('/users/' + new_user_id)
    else:
        return redirect(reverse('users:index'))