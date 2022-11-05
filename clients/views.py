from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from . forms import CreateClientForm, CreateInsuranceForm
from . models import Client, Insurance

def index(request):
    return render(request, "clients/index.html")


"""
CLIENT VIEWS
"""

def list_all_clients(request):
    clients = Client.objects.all()
    return render(request, "clients/clients_list.html", {
        "clients": clients
    })


def client_detail(request, pk):
    client = Client.objects.get(id=pk)
    insurances = Insurance.objects.filter(client_id=pk)
    print(insurances)

    return render(request, "clients/client_detail.html", {
        "client": client,
        "insurances": insurances
    })


def create_client(request):
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
                return redirect(f"/pojistenci/{client.id}/")
            except:
                return redirect("clients:list-all-clients")
    
    return render(request, "clients/create_client.html", {
        "form": form
    })


def edit_client(request, pk):
    client = Client.objects.get(id=pk)
    form = CreateClientForm(instance=client)

    if request.method == "POST":
        form = CreateClientForm(request.POST, instance=client)
        if form.is_valid:
            form.save()
            return redirect(f"/pojistenci/{client.id}/")

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



"""
INSURANCE VIEWS
"""

def insurance_detail(request, pk, id):
    client = Client.objects.get(id=pk)
    insurance = Insurance.objects.get(id=id)

    return render(request, "clients/insurance_detail.html", {
        "client": client,
        "insurance": insurance
    })


def create_insurance(request, pk):
    client = Client.objects.get(id=pk)
    form = CreateInsuranceForm()

    if request.method == "POST":
        form = CreateInsuranceForm(request.POST)
        if form.is_valid:
            insurance = form.save(commit=False)
            insurance.client = client
            insurance.save()
            return redirect("clients:insurance-detail", pk=insurance.client_id, id=insurance.id)

    return render(request,"clients/create_insurance.html", {
        "form": form,
        "client": client
    })


def edit_insurance(request, pk, id):
    insurance = Insurance.objects.get(id=id)
    form = CreateInsuranceForm(instance=insurance)
    
    if request.method == "POST":
        form = CreateInsuranceForm(request.POST, instance=insurance)
        if form.is_valid():
            form.save()
            return redirect("clients:insurance-detail", pk=insurance.client_id, id=insurance.id)

    return render(request, "clients/insurance_edit.html", {
        "form": form
    })


def delete_insurance(request, pk, id):
    insurance = Insurance.objects.get(id=id)

    if request.method == "POST":
        insurance.delete()
        return redirect("clients:client-detail", pk=pk)

    return render(request, "clients/insurance_delete.html", {
        "insurance": insurance
    })
