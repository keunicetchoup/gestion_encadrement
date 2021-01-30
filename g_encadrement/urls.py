
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.urls import path, include

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('enregistrement/', include('enregistrement.urls', namespace='enregistrement')),
    path('admin/', admin.site.urls),
]
