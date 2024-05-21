from django.shortcuts import render

from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        with open("answer.txt", mode="w") as f:
            f.write(name + "\n")
            f.write(phone + "\n")
            f.write(message + "\n")
    return render(request, "contacts.html")

def product(request):
    product = Product.objects.all()
    context = {'products': product}
    return render(request, 'product.html', context)

def one_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product':product}
    return render(request, 'one_product.html', context)

