from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from . forms import CreateClientForm
from . models import Client

def index(request):
    return render(request, "clients/index.html")


def list_all_clients(request):
    clients = Client.objects.all()
    return render(request, "clients/clients_list.html", {
        "clients": clients
    })


def client_detail(request, pk):
    client = Client.objects.get(id=pk)
    return render(request, "clients/client_detail.html", {
        "client": client
    })


def client_create(request):
    """
    Creates client and than redirects to new clients detail. If there are more clients with same email, redirects to all clients list view page.
    """
    form = CreateClientForm()

    if request.method == "POST":
        form = CreateClientForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                client = Client.objects.get(email=request.POST["email"])
                return HttpResponseRedirect(f"/pojistenci/{client.id}/")
            except:
                return redirect("clients:list-all-clients")
    
    return render(request, "clients/client_create.html", {
        "form": form
    })


def edit_client(request, pk):
    client = Client.objects.get(id=pk)
    form = CreateClientForm(instance=client)

    if request.method == "POST":
        form = CreateClientForm(request.POST, instance=client)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(f"/pojistenci/{client.id}/")

    return render(request, "clients/client_edit.html", {
        "client": client,
        "form": form
    })


def delete_client(request, pk):
    client = Client.objects.get(id=pk)
    
    if request.method == "POST":
        client.delete()
        return redirect("clients:list-all-clients")

    return render(request, "clients/client_delete.html", {
        "client": client
    })