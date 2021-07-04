from django.contrib import messages
from django.shortcuts import redirect, render
from contactbook.models import Contact
from contactbook.forms import ContactForm

# Create your views here.
def contactbook_index(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact Saved!")

            return redirect("contactbook_index_page")
    
    form = ContactForm()

    contacts = Contact.objects.all()
    
    return render(request, 'contactbook/index.html', {
        "contacts" : contacts,
        "form" : form
    })

    


def contactbook_show(request, id):

    #to display the single contact page
    try:
        contact = Contact.objects.get(pk=id)
    except Contact.DoesNotExist:
        messages.error(request, "not sure what's wrong")
        return redirect("contactbook_index_page")

    form = None
    #for editting of the single contact
    if request.GET.get("edit") == "true":
        form = ContactForm(instance=contact)
    
    if request.GET.get("edit") == "true" and request.method == "POST":
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            messages.success(request, "Contact Edited!")

            return redirect("contactbook_show_page", contact.id)


    #for delete
    if request.GET.get("delete") == "true" and request.method == "POST":
        contact.delete()
        messages.success(request, "Contact deleted!")

        return redirect("contactbook_index_page")
    

    return render(request, 'contactbook/show.html', {
        "contact" : contact,
        "form" : form
    })

