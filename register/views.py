from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from . forms import RegisterForm

def register(request):
    """User register view that renders page with custom RegisterForm. Automatically logs user in after succesfull registration"""
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)

            return redirect('clients:index')

    else:
        form = RegisterForm()

    return render(request, "register/register.html", {
        "form": form
    })