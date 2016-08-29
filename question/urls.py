from django.conf.urls import url
from . import views
# from .views import BoardViewSet
from django.views.generic.edit import index
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/'

    ), name='register'),
    url(r'^login/$', login, name='login'),
    ]
