from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import Contact

# Create your views here.

def datatable(request):
    list_contact = Contact.objects.all()
    context = {
        'list_contact':list_contact,
    }
    return render(request, 'datatable.html', context)

def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        'form':form,
    }
    if form.is_valid():
        form.save()
        return redirect('datatable')
    return render(request, 'contact.html', context)
