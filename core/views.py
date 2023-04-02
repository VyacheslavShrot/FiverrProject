from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from core.forms import UserForm
from core.services.emails import send_email


class IndexView(TemplateView, FormView):
    template_name = "index.html"
    form_class = UserForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        send_email(request=self.request)

        messages.info(self.request, ' ')
        return super().form_valid(form)
