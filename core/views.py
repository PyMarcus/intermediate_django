from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm, ProductModelForm


def index(request):
    return render(request, 'index.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(name, email, subject, message)
            messages.success(request, "Success! Verify your mail box.")
            form.send_mail()
            form = ContactForm()
        else:
            messages.error(request, "Error to send email")
    context = {
        "form": form
    }
    return render(request, 'contact.html', context)


def product(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)  # create product in the database
        if form.is_valid():
            prod = form.save()
            print(prod.name, prod.price, prod.stoke, prod.image)
            messages.success(request, "Product has been successfully saved")
            form = ProductModelForm()
        else:
            messages.error(request, "Fail to save product")
    else:
        form = ProductModelForm()
    context = {
        'form': form
    }
    return render(request, 'product.html', context)
