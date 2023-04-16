from django.shortcuts import reverse
from django.views import generic
from .models import Contacts
from .forms import ContactModelForm
from django.contrib import messages


class ContactCreateView(generic.CreateView):
    template_name = "contacts/contacts.html"
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse("home:home")

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.save()
        messages.success(self.request, "You have successfully created a New Message")
        return super(ContactCreateView, self).form_valid(form)

