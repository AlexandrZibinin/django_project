from django.shortcuts import render


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
