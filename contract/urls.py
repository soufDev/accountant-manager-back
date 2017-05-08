from django.conf.urls import url

from contract.views import PDFhandle

urlpatterns = [
    url(r'', PDFhandle.as_view()),
]