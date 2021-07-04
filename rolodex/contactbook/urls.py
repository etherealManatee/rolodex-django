from django.urls import path
from contactbook.views import *

urlpatterns = [
    path("", contactbook_index, name='contactbook_index_page'),
    path("show/<uuid:id>", contactbook_show, name="contactbook_show_page")
]
