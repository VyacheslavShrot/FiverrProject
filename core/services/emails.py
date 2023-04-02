from django.template.loader import render_to_string

from django.conf import settings

from django.core.mail import EmailMessage

from core.forms import UserForm


def send_email(request):
    form = UserForm(request.POST, request.FILES)
    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data["name"]
        surname = form.cleaned_data["surname"]
        email = form.cleaned_data["email"]
        phone_number = form.cleaned_data["phone_number"]
        country = form.cleaned_data["country"]
        amount_people = form.cleaned_data["amount_people"]
        budget = form.cleaned_data["budget"]
        desc_project = form.cleaned_data["desc_project"]
        dead_line = form.cleaned_data["dead_line"]
        img = form.cleaned_data.get("img")
        title_of_doc = form.cleaned_data["title_of_doc"]
        screen_play = form.cleaned_data["screen_play"]

    message = render_to_string(
        template_name="emails.html",
        context={
            "name": name,
            "surname": surname,
            "phone_number": phone_number,
            "email": email,
            "country": country,
            "amount_people": amount_people,
            "budget": budget,
            "desc_project": desc_project,
            "dead_line": dead_line,
            "img": img,
            "title_of_doc": title_of_doc,
            "screen_play": screen_play
        }
    )

    email = EmailMessage(
        subject="Film", body=message, to=[settings.EMAIL_HOST_USER]
    )
    email.content_subtype = "html"
    email.send(fail_silently=settings.EMAIL_FAIL_SILENTLY)
