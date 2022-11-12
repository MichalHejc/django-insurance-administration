from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from . forms import CreateClientForm, CreateInsuranceForm
from . models import Client, Insurance


def index(request):
    return render(request, "clients/index.html")


"""
CLIENT VIEWS
"""

@login_required
def list_all_clients(request):
    clients = Client.objects.all()
    return render(request, "clients/clients_list.html", {
        "clients": clients
    })


@login_required
def client_detail(request, pk):
    client = Client.objects.get(id=pk)
    insurances = Insurance.objects.filter(client_id=pk)
    print(insurances)

    return render(request, "clients/client_detail.html", {
        "client": client,
        "insurances": insurances
    })

@staff_member_required(login_url="/login/")
def create_client(request):
    form = CreateClientForm()

    if request.method == "POST":
        form = CreateClientForm(request.POST)
        if form.is_valid():
            client= form.save()
            return redirect(f"/pojistenci/{client.id}/")

    
    return render(request, "clients/create_client.html", {
        "form": form
    })


@staff_member_required(login_url="/login/")
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


@staff_member_required(login_url="/login/")
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

@login_required()
def insurance_detail(request, pk, id):
    client = Client.objects.get(id=pk)
    insurance = Insurance.objects.get(id=id)

    return render(request, "clients/insurance_detail.html", {
        "client": client,
        "insurance": insurance
    })

@staff_member_required(login_url="/login/")
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

@staff_member_required(login_url="/login/")
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

@staff_member_required(login_url="/login/")
def delete_insurance(request, pk, id):
    insurance = Insurance.objects.get(id=id)

    if request.method == "POST":
        insurance.delete()
        return redirect("clients:client-detail", pk=pk)

    return render(request, "clients/insurance_delete.html", {
        "insurance": insurance
    })
