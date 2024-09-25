from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            message = request.POST.get("message", "")

            # Send message and redirect
            email = EmailMessage(
               "The Coffee Shop: New contact message",
               "From {} <{}>\n\nWrote:\n\n{}".format(name, email, message),
               "hello@thecoffeeshop.info",
               ["hello@thecoffeeshop.info"],
               reply_to=[email] 
            )

            try:
                email.send()
                return redirect(reverse("contact")+"?ok")
            except:
                return redirect(reverse("contact")+"?failed")


    return render(request, "contact/contact.html", {"form": contact_form})