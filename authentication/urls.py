from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'', include('authentication.api.urls')),
]
