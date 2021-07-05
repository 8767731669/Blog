from django.conf.urls import include, url
from users.views import dashboard

urlpatterns = [
    url("dashboard/", dashboard, name="dashboard"),
]
